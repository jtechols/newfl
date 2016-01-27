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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('newman_name', models.CharField(max_length=200)),
                ('newman_instrument', models.CharField(max_length=100)),
                ('points', models.IntegerField(default=0)),
                ('imgFileName', models.CharField(max_length=200, null=True)),
                ('woodwind', models.BooleanField(default=False)),
                ('saxophone', models.BooleanField(default=False)),
                ('lowbrass', models.BooleanField(default=False)),
                ('highbrass', models.BooleanField(default=False)),
                ('perc', models.BooleanField(default=False)),
                ('bench', models.BooleanField(default=False)),
                ('flex', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Oldmen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('team_name', models.CharField(max_length=200)),
                ('team_owner', models.CharField(max_length=200)),
                ('team_points', models.IntegerField(default=0)),
                ('locked', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SHB',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shb_name', models.CharField(max_length=200)),
                ('shb_time', models.DateTimeField(verbose_name='Date of SHB')),
                ('limited', models.BooleanField(default=False)),
                ('newman_list', models.ManyToManyField(to='shb.Newman')),
            ],
        ),
        migrations.AddField(
            model_name='newman',
            name='owner',
            field=models.ForeignKey(null=True, blank=True, to='shb.Oldmen'),
        ),
    ]
