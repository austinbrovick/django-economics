# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-09 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('econ', models.CharField(choices=[('microeconomics', 'MICROECONOMICS'), ('macroeconomics', 'MACROECONOMICS')], max_length=30, verbose_name='economics class')),
                ('word', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['word'],
            },
        ),
    ]
