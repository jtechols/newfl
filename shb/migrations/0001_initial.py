# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newman',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('newman_name', models.CharField(max_length=200)),
                ('newman_instrument', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Oldmen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('team_name', models.CharField(max_length=200)),
                ('team_owner', models.CharField(max_length=200)),
                ('newman', models.ForeignKey(to='shb.Newman')),
            ],
        ),
        migrations.CreateModel(
            name='SHB',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('shb_name', models.CharField(max_length=200)),
                ('shb_time', models.DateTimeField(verbose_name='Date of SHB')),
                ('newman', models.ManyToManyField(to='shb.Newman')),
            ],
        ),
    ]
