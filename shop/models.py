from django.db import models

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
    image = models.CharField(max_length=5000)
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
    adresse = models.CharField(max_length=200)
    ville = models.CharField(max_length=200)
    pays = models.CharField(max_length=300)
    zipcode = models.CharField(max_length=300)
    date_commande = models.DateTimeField(auto_now=True)

    class Meta :

        ordering = ['-date_commande']

    
    def __str__(self):
        return self.nom
