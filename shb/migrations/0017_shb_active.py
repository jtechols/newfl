# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0016_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='shb',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
