# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-01-26 06:05
from __future__ import unicode_literals

from django.db import migrations, models
import restaurants.validators


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0006_restaurantlocations_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurantlocations',
            name='category',
            field=models.CharField(blank=True, max_length=120, null=True, validators=[restaurants.validators.category_validator]),
        ),
    ]