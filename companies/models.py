#encoding:utf-8
from django.db import models

class Company( models.Model ):
    ACTIVE     = 'A'
    INACTIVE   = 'I'
    IN_PROCESS = 'P'

    STATUS = (
        ( 'A', 'Activo' ),
        ( 'I', 'Inactivo' ),
        ( 'P', 'En Proceso de activación' ),
    )

    company       = models.CharField( max_length = 200 )
    rfc           = models.CharField( max_length = 15 )
    description   = models.TextField( null = True, blank = True )
    register_date = models.DateTimeField( auto_now = True )
    modify_date   = models.DateTimeField( null = True, blank = True )
    due_date      = models.DateTimeField( null = True, blank = True )
    status        = models.CharField( max_length = 1, choices = STATUS, default = IN_PROCESS )
    web           = models.URLField( null = True, blank = True )

    def __unicode__( self ):
      return self.company