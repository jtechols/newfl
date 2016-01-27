# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shb',
            name='newman',
        ),
        migrations.AddField(
            model_name='shb',
            name='newman',
            field=models.ForeignKey(default=0, to='shb.Newman'),
            preserve_default=False,
        ),
    ]