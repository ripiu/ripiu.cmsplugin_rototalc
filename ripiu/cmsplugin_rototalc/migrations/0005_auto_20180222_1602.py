# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-22 15:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cmsplugin_rototalc', '0004_carouselplugin_header_alignment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carouselplugin',
            name='header_alignment',
        ),
        migrations.RemoveField(
            model_name='carouselplugin',
            name='heading_level',
        ),
        migrations.RemoveField(
            model_name='carouselplugin',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='carouselplugin',
            name='title',
        ),
    ]
