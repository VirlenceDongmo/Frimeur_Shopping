
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('produit/<int:myid>/', views.detail, name='detail'),
    path('checkout', views.checkout, name='panier'),
    path('confirmation', views.confirmation, name='confirmation'),
    path('categorie/<str:foo>', views.categorie, name='categorie'),
    path('A propos', views.about, name='about'),
    path('contacter', views.contact, name='contact'),
    path('contact/', views.contact_view, name='contacter'),
    path('paiement/', views.payment_view, name='paiement'),
    path('paypal/', views.paypal_payment, name='paypal_payment'),
] 






