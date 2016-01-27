# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0013_auto_20160126_2109'),
    ]

    operations = [
        migrations.AddField(
            model_name='newman',
            name='imgFileName',
            field=models.CharField(null=True, max_length=200),
        ),
        migrations.AddField(
            model_name='newman',
            name='saxophone',
            field=models.BooleanField(default=False),
        ),
    ]
