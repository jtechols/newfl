# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0008_auto_20151019_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newman',
            name='owner',
            field=models.ForeignKey(to='shb.Oldmen', null=True, blank=True),
        ),
    ]