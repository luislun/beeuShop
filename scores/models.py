from django.db import models
from django.contrib.auth.models import User

from comments.models   import Comment

class Score( models.Model ):
    ACTIVE         = 'A'
    INACTIVE       = 'I'

    STATUS_CHOICES = (
        ( ACTIVE, 'Activo' ),
        ( INACTIVE, 'Inactivo' ),
    )

    score         = models.DecimalField( max_digits = 5, decimal_places = 2 )
    user          = models.ForeignKey( User )
    status        = models.CharField( max_length = 1, choices = STATUS_CHOICES, default = ACTIVE )
    creation_date = models.DateTimeField( auto_now = True )
    modify_date   = models.DateTimeField( null = True, blank = True )
    comment       = models.ForeignKey( Comment, null = True, blank = True )
    
    def __unicode__( self ):
      return str( self.score )