# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-31 07:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_post_catalog'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='catalog',
            options={'verbose_name': '目录', 'verbose_name_plural': '目录'},
        ),
        migrations.AlterField(
            model_name='catalog',
            name='menu_level',
            field=models.CharField(choices=[('P', '父菜单'), ('S', '子菜单')], max_length=2, verbose_name='目录级别'),
        ),
        migrations.AlterField(
            model_name='catalog',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog', verbose_name='上级目录'),
        ),
        migrations.AlterField(
            model_name='post',
            name='catalog',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.Catalog', verbose_name='目录'),
        ),
    ]
