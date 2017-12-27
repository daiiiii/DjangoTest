# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-23 08:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171019_1644'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': '文章分类', 'verbose_name_plural': '文章分类'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_time'], 'verbose_name': '文章', 'verbose_name_plural': '文章'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': '文章标签', 'verbose_name_plural': '文章标签'},
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(default=0, verbose_name='状态'),
        ),
    ]