import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget
from places import Places
from places.widgets import PlacesWidget
from django.forms.fields import DateField
from .models import Rides, CustomUser


class RidesForm(forms.ModelForm):
    car_model = forms.CharField(max_length=100)
    seats = forms.CharField(max_length=10)
    seats_available = forms.IntegerField()
    cost = forms.CharField(max_length=10)
    start_time = forms.CharField(max_length=100)
    dateofride = DateField(widget=SelectDateWidget)
    message = forms.TextInput()
    source_location = forms.CharField(max_length=1000)
    sou_lati = forms.CharField(max_length=1000)
    sou_long = forms.CharField(max_length=1000)
    des_lati = forms.CharField(max_length=1000)
    des_long = forms.CharField(max_length=1000)
    destination_location = forms.CharField(max_length=1000)

    class Meta:
        model = Rides
        fields = ['car_model', 'seats', 'seats_available', 'cost', 'start_time', 'dateofride', 'message', ]


class UpdateProfileForm(forms.ModelForm):
    gender = forms.CharField(max_length=100)
    dob = forms.CharField(max_length=100)
    mobile = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    ref_number = forms.CharField(max_length=100)
    aadhar = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['gender', 'dob', 'mobile', 'company', 'ref_number', 'aadhar', ]
