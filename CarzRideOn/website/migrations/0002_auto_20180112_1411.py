# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-12 08:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rides',
            name='destination',
            field=models.CharField(blank=True, db_column=b'destination', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='rides',
            name='source',
            field=models.CharField(blank=True, db_column=b'source', max_length=200, null=True),
        ),
    ]