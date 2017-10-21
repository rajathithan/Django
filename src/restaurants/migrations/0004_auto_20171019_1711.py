# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-19 11:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20171017_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantlocations',
            name='modified',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='restaurantlocations',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
