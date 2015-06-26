from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from django.views.generic import ListView, DetailView

from .models import Product, ProductFeature
from categories.models import Category

class ProductList( ListView ):
    model         = Product
    template_name = 'products/product-list.html'

    def get_context_data( self, **kwargs ):
        context = super( ProductList, self ).get_context_data( **kwargs )
        context[ 'categories' ] = Category.objects.filter( primary = False )
        
        return context

class ProductDetailView( DetailView ):
    model               = Product
    context_object_name = 'product'
    template_name       = 'products/product-data-sheet.html'

# def product( request ):
#     productData = get_object_or_404( Product, id=1 )
#     productFeatures = ProductFeature.objects.filter( product = 1 )

#     data = {
#         'product'         : productData,
#         'productFeatures' : productFeatures
#     }

#     return render_to_response( 'products/product-data-sheet.html', data, context_instance = RequestContext( request ) )