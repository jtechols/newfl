# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0014_auto_20160126_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldmen',
            name='current_points',
            field=models.IntegerField(default=0),
        ),
    ]
