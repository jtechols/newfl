# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shb', '0007_oldmen_team_points'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newman',
            name='owner',
            field=models.ForeignKey(null=True, to='shb.Oldmen'),
        ),
    ]