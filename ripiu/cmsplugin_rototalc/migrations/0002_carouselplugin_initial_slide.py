# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 16:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_rototalc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselplugin',
            name='initial_slide',
            field=models.SmallIntegerField(default=0, help_text='Slide to start on.', verbose_name='initial slide'),
        ),
    ]
