from django.contrib import admin
from .models import Product

class ProductAdmin( admin.ModelAdmin ):
    list_display = [ 'id', 'product', 'description', 'price', 'brand' ]

admin.site.register( Product, ProductAdmin )