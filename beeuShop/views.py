from django.views.generic import TemplateView
from categories.models import Category

class HomeView(TemplateView):
    template_name = "beeuShop/home.html"

    def get_context_data( self, **kwargs ):
        context = super( HomeView, self ).get_context_data( **kwargs )
        context[ 'categories' ] = Category.objects.filter( primary = False )
        
        return context
