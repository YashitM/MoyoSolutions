# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Contactus(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    attachment_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contactus'


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Ratings(models.Model):
    rate = models.CharField(max_length=100, blank=True, null=True)
    fb_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ratings'


class Rides(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    seats = models.CharField(max_length=100, blank=True, null=True)
    seats_available = models.IntegerField()
    cost = models.CharField(max_length=10, blank=True, null=True)
    source = models.CharField(max_length=100, blank=True, null=True)
    source_latitude = models.CharField(max_length=100, blank=True, null=True)
    source_longitude = models.CharField(max_length=100, blank=True, null=True)
    destination = models.CharField(max_length=100, blank=True, null=True)
    destination_latitude = models.CharField(max_length=100, blank=True, null=True)
    destination_longitude = models.CharField(max_length=100, blank=True, null=True)
    dateofride = models.CharField(max_length=20, blank=True, null=True)
    start_time = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField()
    message = models.TextField(blank=True, null=True)
    ridecancelstatus = models.IntegerField(db_column='rideCancelStatus')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rides'


class UserRides(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    task_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.DateTimeField()
    message = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_rides'


class Users(models.Model):
    sno = models.AutoField(primary_key=True)
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    mobile = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True)
    dob = models.CharField(max_length=100, blank=True, null=True)
    ref_number = models.CharField(max_length=100, blank=True, null=True)
    ref_status = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    api_key = models.CharField(max_length=32, blank=True, null=True)
    fcm_id = models.CharField(max_length=1000, blank=True, null=True)
    company = models.CharField(max_length=100)
    aadhar = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users'
