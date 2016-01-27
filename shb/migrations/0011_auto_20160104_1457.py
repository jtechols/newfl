# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0010_auto_20160104_1048'),
    ]

    operations = [
        migrations.AddField(
            model_name='newman',
            name='bench',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newman',
            name='perc',
            field=models.BooleanField(default=False),
        ),
    ]