# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('company', models.CharField(max_length=200)),
                ('rfc', models.CharField(max_length=15)),
                ('description', models.TextField()),
                ('register_date', models.DateTimeField(auto_now=True)),
                ('modify_date', models.DateTimeField()),
                ('due_date', models.DateTimeField()),
                ('status', models.CharField(default=b'P', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo'), (b'P', b'En Proceso de activaci\xc3\xb3n')])),
                ('web', models.URLField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
