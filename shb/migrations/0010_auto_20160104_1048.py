# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0009_auto_20151019_1358'),
    ]

    operations = [
        migrations.AddField(
            model_name='newman',
            name='highbrass',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newman',
            name='lowbrass',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newman',
            name='woodwind',
            field=models.BooleanField(default=False),
        ),
    ]
