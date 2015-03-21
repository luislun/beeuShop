from django.db import models

class Features( models.Model):
    feature = models.CharField( max_length = 80 )

    def __unicode__( self ):
      return self.feature