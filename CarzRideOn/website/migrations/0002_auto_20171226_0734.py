# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 02:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrides',
            name='created_at',
            field=models.CharField(max_length=1000),
        ),
    ]