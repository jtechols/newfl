# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0004_auto_20151015_1204'),
    ]

    operations = [
        migrations.AddField(
            model_name='newman',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]