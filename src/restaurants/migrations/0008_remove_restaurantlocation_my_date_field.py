# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-06-30 10:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0007_restaurantlocation_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurantlocation',
            name='my_date_field',
        ),
    ]
