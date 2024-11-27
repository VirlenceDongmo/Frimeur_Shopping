from django.contrib import admin
from .models import Category, Product, Commande

# Register your models here.

admin.site.site_header = "Frimeur-Shopping"
admin.site.site_title = "Frimeur-Shopping"
admin.site.index_title = "Administration"

class CategoryManager(admin.ModelAdmin) :
    list_display = ['name', 'date_added']


class ProductManager(admin.ModelAdmin) :
    list_display = ('title','price','category', 'date_added')
    search_fields= ('title',)
    list_editable = ('price',)

class CommandeManager(admin.ModelAdmin) :
    list_display = ('items','nom','email','date_commande', 'total')

admin.site.register(Category, CategoryManager)
admin.site.register(Product, ProductManager)
admin.site.register(Commande, CommandeManager)