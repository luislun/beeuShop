# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo_file',
            field=models.FileField(upload_to=b'statics/upload/photos'),
            preserve_default=True,
        ),
    ]
