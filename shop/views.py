from django.shortcuts import render, redirect
from .models import Product, Commande, Category, Message, Payment
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required
import json
from django.conf import settings
from shop.API.PaiementMTN.apiDePaiement import PayClass
import uuid
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .forms import PaymentForm
import requests

# Create your views here.

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
def checkout(request) :

    if(request.method == "POST") :
        user = request.user
        nom = user.nom
        total = request.POST.get('total')
        email = user.email
        adresseDeLivraison = request.POST.get('adresseDeLivraison')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        items = request.POST.get('items')
        tel = user.telephone

        com = Commande(items = items, total = total, nom = nom, email = email, adresseDeLivraison = adresseDeLivraison, ville = ville, pays = pays, tel = tel, user_id = user)
        com.save()

        # Convertir les items du panier (JSON) en dictionnaire
        panier = json.loads(items)

        # Préparer les détails de chaque article pour l'e-mail
        article_details = []
        for item_id, details in panier.items():
            nom_article = details[1]
            quantite = details[0]
            prix_unitaire = details[2]
            image = details[3]
            prix_total = quantite * prix_unitaire
            
            # Ajoutez les informations à la liste
            article_details.append(f"""*{nom_article} :
                            - Photo : {image},
                            - Quantité: {quantite},
                            - Prix Total: {prix_total:.2f} FCFA""")

        # Convertir la liste en chaîne
        articles_str = "\n".join(article_details)

        # Envoyer un email

       # subjectForUs = 'Nouvelle commande'
       # messageForUs = f"""
       # Une nouvelle commande a été passée par {nom} depuis Frimeur-Shopping.

        #Détails de la commande :

        #- Email du commanditaire : 
        #    {email}

        #- Adresse de livraison : 
        #    {adresseDeLivraison}

        #- Ville de résidence du commanditaire : 
        #    {ville}

        #- Pays de résidence du commanditaire : 
        #    {pays}

        #- Numéro de téléphone du commanditaire : 
        #    {tel}

        #- Somme totale des commandes : 
        #    {total}

        #- Articles : 
        #{articles_str}

        #"""
        #recipient_list = ['dongmofeudjio5@gmail.com']

        #send_mail(subjectForUs, messageForUs, settings.EMAIL_HOST_USER, recipient_list)

        #subjectForHer = 'Demande de confirmation depuis Frimeur-Shopping'

        #messageForHer = f"""
        #Nous vous sommes reconnaissants pour votre confiance Mr/Mme/Mslle {nom}.
        
        #Si vous rencontrez des problèmes pour vos opérations sur notre plateforme, à défaut de nous contacter #par email, vous pouvez le faire via notre numéro whatsapp suivant : 6 54 15 81 75 .
        #"""

        #recipient_list = {email}

        #send_mail(subjectForHer,messageForHer,settings.EMAIL_HOST_USER,recipient_list)

        return redirect('paiement')

    return render(request,"shop/checkout.html")


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


@csrf_exempt  # Désactivez la protection CSRF pour cette vue (à utiliser avec précaution)
def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment_data = form.cleaned_data
            payment = Payment.objects.create(
                amount=payment_data['amount'],
                phone_number=payment_data.get('phone_number'),
                card_number=payment_data.get('card_number'),
                expiry_date=payment_data.get('expiry_date'),
                cvv=payment_data.get('cvv'),
                status='pending'
            )

            if payment_data['payment_method'] == 'mtn':
                # Appel à l'API MTN Mobile Money
                response = requests.post('https://api.mtn.com/checkout', json={
                    'amount': payment_data['amount'],
                    'phone': payment_data['phone_number']
                })
            elif payment_data['payment_method'] == 'orange':
                # Appel à l'API Orange Money
                response = requests.post('https://api.orange.com/checkout', json={
                    'amount': payment_data['amount'],
                    'phone': payment_data['phone_number']
                })
            elif payment_data['payment_method'] == 'card':
                # Appel à l'API de paiement par carte
                response = requests.post('https://api.cardpayment.com/checkout', json={
                    'amount': payment_data['amount'],
                    'card_number': payment_data['card_number'],
                    'expiry_date': payment_data['expiry_date'],
                    'cvv': payment_data['cvv']
                })

            if response.status_code == 200:
                payment.status = 'completed'
                payment.save()
               # return redirect('success')  # Redirigez vers une page de succès
            else:
                return render(request, 'paiement.html', {'form': form, 'error': response.json().get('message')})

    else:
        form = PaymentForm()
    return render(request, 'shop/paiement.html', {'form': form})

