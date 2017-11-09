# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_rototalc_carouselplugin', serialize=False, to='cms.CMSPlugin')),
                ('name', models.SlugField(max_length=30, verbose_name='name')),
                ('show_arrows', models.BooleanField(default=True, help_text='Enable Next/Prev arrows.', verbose_name='show arrows')),
                ('autoplay', models.BooleanField(default=True, help_text='Enable auto play of slides.', verbose_name='autoplay')),
                ('autoplay_speed', models.SmallIntegerField(default=3000, help_text='Auto play change interval (in milliseconds).', verbose_name='autoplay speed')),
                ('slides_to_show', models.SmallIntegerField(default=1, help_text='Number of slides to show at a time.', verbose_name='slides to show')),
                ('center_mode', models.BooleanField(default=True, help_text='Enable centered view with partial prev/next slides. Use with odd numbered slidesToShow counts.', verbose_name='center mode')),
                ('dots', models.BooleanField(default=True, help_text='Show current slide indicator dots.', verbose_name='show dots')),
                ('focus_on_select', models.BooleanField(default=False, help_text='Enable focus on selected element (click).', verbose_name='focus on select')),
                ('infinite', models.BooleanField(default=True, help_text='Infinite looping.', verbose_name='infinite')),
                ('speed', models.SmallIntegerField(default=1, help_text='Transition speed.', verbose_name='slides to show')),
                ('vertical', models.BooleanField(default=False, verbose_name='slide direction')),
            ],
            options={
                'verbose_name': 'Carousel',
                'verbose_name_plural': 'Carousels',
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SlidePlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='cmsplugin_rototalc_slideplugin', serialize=False, to='cms.CMSPlugin')),
                ('caption_text', models.CharField(blank=True, default='', max_length=400, verbose_name='caption')),
            ],
            options={
                'verbose_name': 'Generic slide',
                'verbose_name_plural': 'Generic slides',
            },
            bases=('cms.cmsplugin',),
        ),
    ]
