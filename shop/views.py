from django.shortcuts import render, redirect
from .models import Product, Commande, Category
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail

# Create your views here.

def index(request) :

    product_object = Product.objects.all()

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


def checkout(request) :

    if(request.method == "POST") :
        nom = request.POST.get('nom')
        total = request.POST.get('total')
        email = request.POST.get('email')
        adresseDeLivraison = request.POST.get('adresseDeLivraison')
        ville = request.POST.get('ville')
        pays = request.POST.get('pays')
        items = request.POST.get('items')
        tel = request.POST.get('tel')
        user = request.user
        paiement = request.POST.get('paiement')

        com = Commande(items = items, total = total, nom = nom, email = email, adresseDeLivraison = adresseDeLivraison, ville = ville, pays = pays, tel = tel, paiement = paiement, user_id = user)
        com.save()

        # Envoyer un email

        subject = 'Nouvelle commande'
        message = f"""
        Une nouvelle commande a été passée par {nom} depuis Frimeur-Shopping.

        Détails de la commande :

        - Email du commanditaire : {email}

        - Adresse de livraison : {adresseDeLivraison}

        - Ville de résidence du commanditaire : {ville}

        - Pays de résidence du commanditaire : {pays}

        - Numéro de téléphone du commanditaire : {tel}

        - Somme totale des commandes : {total}

        - Mode de paiement : {paiement}

        - Articles : {items}

        """
        from_email = 'dongmovirlence@gmail.com'
        recipient_list = ['dongmofeudjio5@gmail.com']

        send_mail(subject, message, from_email, recipient_list)

        return redirect('confirmation')

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
    