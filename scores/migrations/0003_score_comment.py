# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20150321_2056'),
        ('scores', '0002_score_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='score',
            name='comment',
            field=models.ForeignKey(blank=True, to='comments.Comment', null=True),
            preserve_default=True,
        ),
    ]
