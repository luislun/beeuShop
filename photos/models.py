from django.db import models

class Photo( models.Model ):
    ACTIVE         = 'A'
    INACTIVE       = 'I'

    STATUS_CHOICES = (
        ( ACTIVE, 'Activo' ),
        ( INACTIVE, 'Inactivo' ),
    )

    photo_file    = models.FileField( upload_to = 'statics/upload/photos' )
    status        = models.CharField( max_length = 1, choices = STATUS_CHOICES, default = ACTIVE )
    creation_date = models.DateTimeField( auto_now = True )

    def __unicode__( self ):
      return unicode( self.photo_file ) or u''