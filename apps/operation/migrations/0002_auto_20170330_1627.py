# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-30 16:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='coursecomments',
            options={'verbose_name': 'Comments', 'verbose_name_plural': 'Comments'},
        ),
    ]