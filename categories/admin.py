from django.contrib import admin
from .models import Category

class CategoryAdmin( admin.ModelAdmin ):
    list_display = [ 'category', 'primary', 'parent' ]

admin.site.register( Category, CategoryAdmin )
