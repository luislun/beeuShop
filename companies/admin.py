from django.contrib import admin
from .models import Company

class CompanyAdmin( admin.ModelAdmin ):
    list_display = [ 'company', 'rfc', 'description', 'register_date', 'modify_date', 'due_date', 'status', 'web' ]

admin.site.register( Company, CompanyAdmin )
