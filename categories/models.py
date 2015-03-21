from django.db import models

class Category( models.Model ):
    category = models.CharField( max_length = 100 )
    primary  = models.BooleanField( default = False )
    parent   = models.ForeignKey( "self", related_name = "children", null=True, blank=True )
    
    def __unicode__( self ):
      return self.category