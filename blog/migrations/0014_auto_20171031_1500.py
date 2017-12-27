# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 07:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_auto_20171031_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='catalog',
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.Tag', verbose_name='标签'),
        ),
    ]
