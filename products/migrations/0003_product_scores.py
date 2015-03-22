# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scores', '0002_score_user'),
        ('products', '0002_product_creation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='scores',
            field=models.ManyToManyField(to='scores.Score', null=True, blank=True),
            preserve_default=True,
        ),
    ]
