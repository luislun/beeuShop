# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.DecimalField(max_digits=5, decimal_places=2)),
                ('status', models.CharField(default=b'A', max_length=1, choices=[(b'A', b'Activo'), (b'I', b'Inactivo')])),
                ('creation_date', models.DateTimeField(auto_now=True)),
                ('modify_date', models.DateTimeField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
