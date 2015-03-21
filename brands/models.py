from django.db import models

class Brand( models.Model ):
    brand = models.CharField( max_length = 50 )
    web   = models.URLField( max_length = 200 )

    def __unicode__( self ):
      return self.brand