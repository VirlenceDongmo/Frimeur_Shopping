from django.db import models
from Authentification_du_systeme.models import CustomUser
from django import forms

# Create your models here.

class Category(models.Model) :

    name  = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    class Meta :

        ordering = ['date_added']

    def __str__(self) -> str:
        return self.name
    


class Size(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    

class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Product(models.Model) :

    title = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/', blank = True)
    date_added = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    sizes = models.ManyToManyField(Size)

    colors = models.ManyToManyField(Color)

    class Meta :

        ordering = ['-date_added']

    def __str__(self) -> str:
        return self.title
    


class Commande(models.Model) :

    STATUS_CHOICES = (
        ('en cours', 'En cours'),
        ('complétée', 'Complétée')
    )

    items = models.CharField(max_length=300)
    total = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    email = models.EmailField()
    adresseDeLivraison = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    tel = models.BigIntegerField()
    status = models.CharField(default='en cours', max_length=30)

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="commande")

    class Meta :

        ordering = ['-date_commande']

    
    def __str__(self):
        return self.nom


class Message(models.Model) :

    nom = models.CharField(max_length=300)
    email = models.EmailField()
    message = models.CharField(max_length=1000)
    date_added = models.DateTimeField(auto_now=True)

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="message")

    class Meta :

        ordering = ['-date_added']

    
    def __str__(self):
        return self.nom
    


class Payment(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    date_added = models.DateTimeField(auto_now=True)
    
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)

    class Meta :

        ordering = ['-date_added']
