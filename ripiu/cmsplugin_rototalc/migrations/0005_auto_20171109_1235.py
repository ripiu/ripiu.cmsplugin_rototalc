# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_rototalc', '0004_auto_20171109_1218'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselplugin',
            name='vertical',
        ),
        migrations.AlterField(
            model_name='carouselplugin',
            name='height',
            field=models.CharField(default='', help_text='', max_length=10, verbose_name='height'),
        ),
    ]
