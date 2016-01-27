# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0003_auto_20151015_1059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newman',
            name='shb_list',
        ),
        migrations.AddField(
            model_name='shb',
            name='newman_list',
            field=models.ManyToManyField(to='shb.Newman'),
        ),
    ]