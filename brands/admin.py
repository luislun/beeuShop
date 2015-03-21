from django.contrib import admin
from .models import Brand

class BrandAdmin( admin.ModelAdmin ):
    list_display = [ 'brand', 'web' ]

admin.site.register( Brand, BrandAdmin )
