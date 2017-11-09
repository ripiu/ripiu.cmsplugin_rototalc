# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 11:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_rototalc', '0002_carouselplugin_variable_width'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselplugin',
            name='height',
            field=models.CharField(default='', help_text='', max_length=10, verbose_name='height'),
        ),
        migrations.AlterField(
            model_name='carouselplugin',
            name='speed',
            field=models.SmallIntegerField(default=300, help_text='Transition speed.', verbose_name='speed'),
        ),
    ]
