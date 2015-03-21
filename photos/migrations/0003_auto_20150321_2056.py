# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20150321_2009'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='creation_date',
            field=models.DateTimeField(auto_now=True),
            preserve_default=True,
        ),
    ]
