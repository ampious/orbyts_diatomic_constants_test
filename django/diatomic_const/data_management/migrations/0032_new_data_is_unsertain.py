# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-07-26 16:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_management', '0031_auto_20180726_1537'),
    ]

    operations = [
        migrations.AddField(
            model_name='new_data',
            name='is_unsertain',
            field=models.BooleanField(default=False),
        ),
    ]