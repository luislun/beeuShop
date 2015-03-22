from django.contrib import admin
from .models import Score

class ScoreAdmin( admin.ModelAdmin ):
    list_display = [ 'score', 'user', 'creation_date', 'modify_date' ]

admin.site.register( Score, ScoreAdmin )
