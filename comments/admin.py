from django.contrib import admin
from .models import Comment

class CommentsAdmin( admin.ModelAdmin ):
    list_display = [ 'id', 'comment', 'creation_date', 'due_date', 'user', 'status' ]

admin.site.register( Comment, CommentsAdmin )
