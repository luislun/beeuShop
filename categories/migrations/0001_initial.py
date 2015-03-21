# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=100)),
                ('primary', models.BooleanField(default=False)),
                ('parent', models.ForeignKey(related_name='children', blank=True, to='categories.Category', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
