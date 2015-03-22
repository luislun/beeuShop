#encoding:utf-8
from django.db import models
from django.utils import timezone

from brands.models     import Brand
from categories.models import Category 
from comments.models   import Comment
from features.models   import Features
from photos.models     import Photo
from scores.models     import Score

class Product( models.Model ):
    product          = models.CharField( max_length = 100 )
    description      = models.CharField( max_length = 250, null = True, blank = True )
    long_description = models.TextField( null = True, blank = True  )
    price            = models.DecimalField( max_digits = 20, decimal_places = 6 )
    creation_date    = models.DateTimeField( auto_now = True, default = timezone.now )

    brand            = models.ForeignKey( Brand )
    category_level_1 = models.ForeignKey( Category, related_name = 'category_level_1' )
    category_level_2 = models.ForeignKey( Category, related_name = 'category_level_2', null = True, blank = True )
    category_level_3 = models.ForeignKey( Category, related_name = 'category_level_3', null = True, blank = True )
    category_level_4 = models.ForeignKey( Category, related_name = 'category_level_4', null = True, blank = True )
    category_level_5 = models.ForeignKey( Category, related_name = 'category_level_5', null = True, blank = True )

    photos           = models.ManyToManyField( Photo, null = True, blank = True )
    scores           = models.ManyToManyField( Score, null = True, blank = True )
    relatedProducts  = models.ManyToManyField( 'self', related_name = 'related_products', null = True, blank = True )

    def __unicode__( self ):
      return self.product


class ProductFeature( models.Model ):
    product     = models.ForeignKey( Product )
    feature     = models.ForeignKey( Features )
    description = models.CharField( max_length = 250 )

    def __unicode__( self ):
      return  unicode( self.product ) or u''
