# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0005_newman_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='shb',
            name='limited',
            field=models.BooleanField(default=False),
        ),
    ]