from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext

from .models import Product, ProductFeature

def product( request ):
    productData = get_object_or_404( Product, id=1 )
    productFeatures = ProductFeature.objects.filter( product = 1 )

    data = {
        'product'         : productData,
        'productFeatures' : productFeatures
    }

    return render_to_response('product-data-sheet-product.html', data, context_instance=RequestContext(request))