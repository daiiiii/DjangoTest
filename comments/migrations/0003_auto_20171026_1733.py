# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-26 09:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20171026_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='phone',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unit',
            field=models.CharField(max_length=100),
        ),
    ]
