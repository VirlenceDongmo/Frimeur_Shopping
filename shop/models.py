from django.db import models
from Authentification_du_systeme.models import CustomUser

# Create your models here.

class Category(models.Model) :

    name  = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    class Meta :

        ordering = ['date_added']

    def __str__(self) -> str:
        return self.name



class Product(models.Model) :

    title = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    image = models.ImageField(upload_to = 'media/', blank = True)
    date_added = models.DateTimeField(auto_now=True)

    category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    class Meta :

        ordering = ['-date_added']

    def __str__(self) -> str:
        return self.title
    


class Commande(models.Model) :

    items = models.CharField(max_length=300)
    total = models.CharField(max_length=300)
    nom = models.CharField(max_length=300)
    email = models.EmailField()
    localisation = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)
    tel = models.BigIntegerField()

    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE,related_name="commande")

    class Meta :

        ordering = ['-date_commande']

    
    def __str__(self):
        return self.nom
