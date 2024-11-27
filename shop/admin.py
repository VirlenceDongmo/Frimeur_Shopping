from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.

class CategoryManager(admin.ModelAdmin) :
    list_display = ['name', 'date_added']


class ProductManager(admin.ModelAdmin) :
    list_display = ('title','price','category', 'date_added')


class CommandeManager(admin.ModelAdmin) :
    list_display = ('items','nom','email','date_commande', 'total')

admin.site.register(Category, CategoryManager)
admin.site.register(Product, ProductManager)
admin.site.register(Commande, CommandeManager)