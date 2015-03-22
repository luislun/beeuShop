from django.contrib import admin
from .models import Product, ProductFeature

class ProductAdmin( admin.ModelAdmin ):
    list_display = [ 'id', 'product', 'description', 'price', 'brand' ]

admin.site.register( Product, ProductAdmin )


class ProductFeatureAdmin( admin.ModelAdmin ):
    list_display = [ 'product', 'feature', 'description' ]

admin.site.register( ProductFeature, ProductFeatureAdmin )