# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 23:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0002_definition'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='definition',
            options={'ordering': ['-votes'], 'verbose_name': 'definition'},
        ),
    ]
