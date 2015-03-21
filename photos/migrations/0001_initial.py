# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('photo_file', models.FileField(upload_to=b'static/upload/photos')),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('creation_date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
