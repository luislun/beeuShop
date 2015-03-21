from django.db import models
from django.contrib.auth.models import User

class Comment( models.Model ):
    ACTIVE         = 'A'
    INACTIVE       = 'I'
    STATUS_CHOICES = (
        ( ACTIVE, 'Activo' ),
        ( INACTIVE, 'Inactivo' ),
    )

    comment       = models.TextField()
    user          = models.ForeignKey( User )
    creation_date = models.DateTimeField( auto_now = True )
    due_date      = models.DateTimeField( null=True, blank=True)
    status        = models.CharField( max_length=1, choices=STATUS_CHOICES, default=ACTIVE )


    def __unicode__( self ):
      return self.comment