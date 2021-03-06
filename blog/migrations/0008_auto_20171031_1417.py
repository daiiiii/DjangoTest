# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 06:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_catalog'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='post',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Post'),
        ),
    ]
