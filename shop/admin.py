from django.contrib import admin
from .models import Category, Product

# Register your models here.

class CategoryManager(admin.ModelAdmin) :
    list_display = ['name', 'date_added']


class ProductManager(admin.ModelAdmin) :
    list_display = ('title','price','category', 'date_added')

admin.site.register(Category, CategoryManager)
admin.site.register(Product, ProductManager)