# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0011_auto_20160104_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='newman',
            name='flex',
            field=models.BooleanField(default=False),
        ),
        migrations.RemoveField(
            model_name='newman',
            name='saxophone',
            field=models.BooleanField(default=False),
        ),
    ]
