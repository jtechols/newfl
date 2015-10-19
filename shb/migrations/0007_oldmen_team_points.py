# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0006_shb_limited'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldmen',
            name='team_points',
            field=models.IntegerField(default=0),
        ),
    ]
