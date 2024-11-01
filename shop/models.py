from django.db import models

# Create your models here.

class Category(models.Model) :

    name  = models.CharField(max_length=500)
    date_added = models.DateTimeField(auto_now=True)

    class Meta :

        odering = ['date_added']



class Product(models.Model) :

    title = models.CharField(max_length=500)
    price = models.FloatField()
    description = models.TextField()
    image = models.CharField(max_length=5000)
    date_added = models.DateTimeField(auto_now=True)

    Category = models.ForeignKey(Category, related_name='category', on_delete=models.CASCADE)

    class Meta :

        odering = ['date_added']
    
