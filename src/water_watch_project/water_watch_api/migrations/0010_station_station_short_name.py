# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-24 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water_watch_api', '0009_station_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='station_short_name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
