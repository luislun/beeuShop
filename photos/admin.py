from django.contrib import admin
from .models import Photo

class PhotoAdmin( admin.ModelAdmin ):
    list_display = [ 'photo_file', 'status', 'creation_date' ]

admin.site.register( Photo, PhotoAdmin )
