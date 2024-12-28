from django.shortcuts import render, redirect
from .models import Product, Commande, Category, Message, Payment
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import json
from django.conf import settings
from .forms import PaymentForm



def index(request) :

    product_object = Product.objects.all().prefetch_related('sizes','colors')

    item_name = request.GET.get("item-name")

    if item_name != '' and item_name is not None :
        product_object = Product.objects.filter(title__icontains = item_name)

    paginator = Paginator(product_object, 4)
    page = request.GET.get('page')

    product_object = paginator.get_page(page)

    return render(request,"shop/index.html", {'product_object' : product_object})


def detail(request, myid) :

    product_object = Product.objects.get(id = myid)

    return render(request, "shop/detail.html", {'product':product_object})


@login_required(login_url='login_view')
def checkout(request):
    if request.method == "POST":
        user = request.user
        nom = user.nom
        total = request.POST.get('total')
        email = user.email
        adresseDeLivraison = request.POST.get('adresseDeLivraison')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        items = request.POST.get('items')
        tel = user.telephone

        com = Commande.objects.create(
            items=items,
            total=total,
            nom=nom,
            email=email,
            adresseDeLivraison=adresseDeLivraison,
            ville=ville,
            pays=pays,
            tel=tel,
            user_id=user
        )
        
        request.session['commande_id'] = com.id

        panier = json.loads(items)
        article_details = []
        for item_id, details in panier.items():
            nom_article = details[1]
            quantite = details[0]
            prix_unitaire = details[2]
            image = details[3]
            prix_total = quantite * prix_unitaire
            
            article_details.append(f"""*{nom_article} :
                            - Photo : {image},
                            - Quantité: {quantite},
                            - Prix Total: {prix_total:.2f} FCFA""")

        articles_str = "\n".join(article_details)
        subjectForUs = 'Nouvelle commande'
        messageForUs = f"""
        Une nouvelle commande a été passée par {nom} depuis Frimeur-Shopping.

        Détails de la commande :
        - Email : {email}
        - Adresse de livraison : {adresseDeLivraison}
        - Ville : {ville}
        - Pays : {pays}
        - Téléphone : {tel}
        - Total : {total}
        - Articles : {articles_str}
        """
        
        recipient_list = ['dongmofeudjio5@gmail.com']
        send_mail(subjectForUs, messageForUs, settings.EMAIL_HOST_USER, recipient_list)

        return redirect('paiement') 

    return render(request, "shop/checkout.html")


def confirmation(request) :

    info = Commande.objects.all()[:1]
    for item in info :
        nom = item.nom

    return render(request,"shop/confirmation.html", {'name':nom})


def categorie(request, foo) :

    foo = foo.replace('-',' ')

    try :
        categorie = Category.objects.get(name = foo)
        products = Product.objects.filter(category = categorie)

        paginator = Paginator(products, 4)
        page = request.GET.get('page')

        products = paginator.get_page(page)

        return render(request, "shop/categories.html",{'products':products, 'categorie':categorie})
    
    except :
        
        return redirect ('home')
    


def about(request):
    return render(request, 'shop/about.html')
    

@login_required(login_url='login_view')
def contact(request):
    return render(request, 'shop/contact.html')


def contact_view(request):
    if request.method == 'POST':
        user = request.user
        nom = user.nom
        email = user.email
        message = request.POST.get('message')

        messageSave = Message(user_id = user, nom = nom, email = email, message = message)
        messageSave.save()

        subject = f'Nouveau message de {nom} depuis Frimeur-Shopping'
        body = f'Message de {nom} ({email}):\n\n{message}'
        recipient_list = ['dongmofeudjio5@gmail.com']  

        messages.success(request, "Votre message a bien été reçu. Nous vous remercions pour votre participation.")

        send_mail(subject, body, settings.EMAIL_HOST_USER, recipient_list)

        return redirect('contact')  

    return render(request, 'contact.html')


def payment_view(request):
    if request.method == 'POST':
        user = request.user
        email = user.email
        commande_id = request.session.get('commande_id') 

        try:
            commande = Commande.objects.get(id=commande_id)
            total = commande.total
            payment_method = request.POST['payment_method']
            phone = request.POST['phone_number']

            if payment_method == 'mtn':
                subject = 'Demande de confirmation depuis Frimeur-Shopping'
                message = f"Vous avez choisi de payer {total} par MTN Mobile Money. Numéro du compte : 6 54 15 81 75."
            elif payment_method == 'orange':
                subject = 'Demande de confirmation depuis Frimeur-Shopping'
                message = f"Vous avez choisi de payer {total} par Orange Money. Numéro du compte : 6 56 93 19 87."

            send_mail(subject, message, settings.EMAIL_HOST_USER, [email])

            Payment.objects.create(
                amount= total,
                phone_number= phone,
                user_id=user,
                commande=commande
            )

            messages.success(request, 'Le paiement a été traité avec succès.')
            return redirect('confirmation')

        except Commande.DoesNotExist:
            messages.error(request, 'Commande introuvable.')
        except Exception as e:
            messages.error(request, f'Erreur: {str(e)}')
    form = PaymentForm()
    return render(request, 'shop/paiement.html', {'form': form})