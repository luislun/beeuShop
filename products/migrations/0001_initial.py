# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('features', '0001_initial'),
        ('brands', '0001_initial'),
        ('photos', '0002_auto_20150321_2009'),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=250, null=True, blank=True)),
                ('long_description', models.TextField(null=True, blank=True)),
                ('price', models.DecimalField(max_digits=20, decimal_places=6)),
                ('brand', models.ForeignKey(to='brands.Brand')),
                ('category_level_1', models.ForeignKey(related_name='category_level_1', to='categories.Category')),
                ('category_level_2', models.ForeignKey(related_name='category_level_2', blank=True, to='categories.Category', null=True)),
                ('category_level_3', models.ForeignKey(related_name='category_level_3', blank=True, to='categories.Category', null=True)),
                ('category_level_4', models.ForeignKey(related_name='category_level_4', blank=True, to='categories.Category', null=True)),
                ('category_level_5', models.ForeignKey(related_name='category_level_5', blank=True, to='categories.Category', null=True)),
                ('comments', models.ManyToManyField(to='comments.Comment', null=True, blank=True)),
                ('features', models.ManyToManyField(to='features.Features', null=True, blank=True)),
                ('photos', models.ManyToManyField(to='photos.Photo', null=True, blank=True)),
                ('relatedProducts', models.ManyToManyField(related_name='relatedProducts_rel_+', null=True, to='products.Product', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
