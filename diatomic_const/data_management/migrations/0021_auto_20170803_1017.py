# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-03 10:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0020_auto_20170802_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='molecular_state',
            name='total_angular_momentum',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]