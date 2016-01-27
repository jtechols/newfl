# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0012_auto_20160106_0938'),
    ]

    operations = [
        migrations.AddField(
            model_name='oldmen',
            name='locked',
            field=models.BooleanField(default=False),
        ),
    ]
