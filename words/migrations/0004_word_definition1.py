# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 02:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0003_auto_20160509_2353'),
    ]

    operations = [
        migrations.AddField(
            model_name='word',
            name='definition1',
            field=models.TextField(default='testing'),
            preserve_default=False,
        ),
    ]