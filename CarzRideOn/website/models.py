from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin, User
from django.db import models
from places.fields import PlacesField


class Contactus(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=11, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    attachment_url = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        db_table = 'contactus'


class Ratings(models.Model):
    rate = models.CharField(max_length=100, blank=True, null=True)
    fb_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'ratings'


class Rides(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    car_model = models.CharField(max_length=100, blank=True, null=True)
    seats = models.CharField(max_length=100, blank=True, null=True, db_column='seats')
    seats_available = models.IntegerField(db_column='seats_available')
    cost = models.CharField(max_length=10, blank=True, null=True, db_column='cost')
    source = models.CharField(max_length=100, blank=True, null=True, db_column='source')
    source_latitude = models.CharField(max_length=100, blank=True, null=True, db_column='source_latitude')
    source_longitude = models.CharField(max_length=100, blank=True, null=True, db_column='source_longitude')
    destination = models.CharField(max_length=100, blank=True, null=True, db_column='destination')
    destination_latitude = models.CharField(max_length=100, blank=True, null=True, db_column='destination_latitude')
    destination_longitude = models.CharField(max_length=100, blank=True, null=True, db_column='destination_longitude')
    dateofride = models.CharField(max_length=20, blank=True, null=True, db_column='dateofride')
    start_time = models.CharField(max_length=100, blank=True, null=True, db_column='start_time')
    created_at = models.DateTimeField(db_column='created_at')
    message = models.TextField(blank=True, null=True, db_column='message')
    ridecancelstatus = models.IntegerField(db_column='rideCancelStatus')  # Field name made lowercase.

    class Meta:
        db_table = 'rides'

class UserRides(models.Model):
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    task_id = models.CharField(max_length=100, blank=True, null=True)
    status = models.CharField(max_length=1, blank=True, null=True)
    created_at = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'user_rides'


# Create your models here.
class CustomUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, unique=True)
    sno = models.AutoField(primary_key=True)
    fb_id = models.CharField(max_length=100, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True, unique=True, default="")
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
        db_table = 'users'
