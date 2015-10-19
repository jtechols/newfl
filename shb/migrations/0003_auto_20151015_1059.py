# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0002_auto_20151015_1050'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oldmen',
            name='newman',
        ),
        migrations.RemoveField(
            model_name='shb',
            name='newman',
        ),
        migrations.AddField(
            model_name='newman',
            name='owner',
            field=models.ForeignKey(to='shb.Oldmen', default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newman',
            name='shb_list',
            field=models.ManyToManyField(to='shb.SHB'),
        ),
    ]
