from django.contrib import admin
from .models import Score

class ScoreAdmin( admin.ModelAdmin ):
    list_display = [ 'score', 'creation_date', 'modifie_date' ]

admin.site.register( Score, ScoreAdmin )
