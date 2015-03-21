from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import Product

def product( request ):
    productData = get_object_or_404( Product, id=1 )

    return render_to_response('product-data-sheet-product.html', { 'product': productData }, context_instance=RequestContext(request))