# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-29 20:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20170329_2058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(choices=[('male', 'Male'), ('female', 'Female')], default='female', max_length=20),
        ),
    ]