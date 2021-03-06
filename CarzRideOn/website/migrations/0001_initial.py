# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-11 16:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True)),
                ('type', models.CharField(blank=True, max_length=11, null=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('attachment_url', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'contactus',
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True)),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.CharField(blank=True, default=b'', max_length=100, null=True, unique=True)),
                ('mobile', models.CharField(blank=True, max_length=100, null=True)),
                ('gender', models.CharField(blank=True, max_length=100, null=True)),
                ('dob', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_number', models.CharField(blank=True, max_length=100, null=True)),
                ('ref_status', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField()),
                ('api_key', models.CharField(blank=True, max_length=32, null=True)),
                ('fcm_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('company', models.CharField(max_length=100)),
                ('aadhar', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='Ratings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(blank=True, max_length=100, null=True)),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
        migrations.CreateModel(
            name='Rides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True)),
                ('car_model', models.CharField(blank=True, max_length=100, null=True)),
                ('seats', models.CharField(blank=True, db_column=b'seats', max_length=100, null=True)),
                ('seats_available', models.IntegerField(db_column=b'seats_available')),
                ('cost', models.CharField(blank=True, db_column=b'cost', max_length=10, null=True)),
                ('source', models.CharField(blank=True, db_column=b'source', max_length=100, null=True)),
                ('source_latitude', models.CharField(blank=True, db_column=b'source_latitude', max_length=100, null=True)),
                ('source_longitude', models.CharField(blank=True, db_column=b'source_longitude', max_length=100, null=True)),
                ('destination', models.CharField(blank=True, db_column=b'destination', max_length=100, null=True)),
                ('destination_latitude', models.CharField(blank=True, db_column=b'destination_latitude', max_length=100, null=True)),
                ('destination_longitude', models.CharField(blank=True, db_column=b'destination_longitude', max_length=100, null=True)),
                ('dateofride', models.CharField(blank=True, db_column=b'dateofride', max_length=20, null=True)),
                ('start_time', models.CharField(blank=True, db_column=b'start_time', max_length=100, null=True)),
                ('created_at', models.DateTimeField(db_column=b'created_at')),
                ('message', models.TextField(blank=True, db_column=b'message', null=True)),
                ('ridecancelstatus', models.IntegerField(db_column=b'rideCancelStatus')),
            ],
            options={
                'db_table': 'rides',
            },
        ),
        migrations.CreateModel(
            name='UserRides',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fb_id', models.CharField(blank=True, max_length=100, null=True)),
                ('task_id', models.CharField(blank=True, max_length=100, null=True)),
                ('status', models.CharField(blank=True, max_length=1, null=True)),
                ('created_at', models.CharField(max_length=1000)),
                ('message', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'db_table': 'user_rides',
            },
        ),
    ]
