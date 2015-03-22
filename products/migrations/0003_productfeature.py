# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0001_initial'),
        ('products', '0002_product_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=250)),
                ('feature', models.ForeignKey(to='features.Features')),
                ('product', models.ForeignKey(to='products.Product')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
