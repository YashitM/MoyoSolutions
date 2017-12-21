import datetime
from django import forms
from django.contrib.admin.widgets import AdminDateWidget
from django.forms import SelectDateWidget
from places import Places
from places.widgets import PlacesWidget
from django.forms.fields import DateField
from .models import Rides, DestinationLocation, CustomUser


class RidesForm(forms.ModelForm):
    car_model = forms.CharField(max_length=100)
    seats = forms.CharField(max_length=10)
    seats_available = forms.IntegerField()
    cost = forms.CharField(max_length=10)
    start_time = forms.CharField(max_length=100)
    dateofride = DateField(widget=SelectDateWidget)
    message = forms.TextInput()

    class Meta:
        model = Rides
        fields = ['car_model', 'seats', 'seats_available', 'cost', 'start_time', 'dateofride', 'message', ]


class PlacesField(forms.MultiValueField):
    default_error_messages = {
        'invalid': ('Enter a valid geoposition.')
    }

    def __init__(self, *args, **kwargs):
        fields = (
            forms.CharField(label=('place')),
            forms.DecimalField(label=('Latitude')),
            forms.DecimalField(label=('Longitude')),
        )
        if 'initial' in kwargs:
            kwargs['initial'] = Places(*kwargs['initial'].split(','))
        self.widget = PlacesWidget()
        super(PlacesField, self).__init__(fields, **kwargs)

    def widget_attrs(self, widget):
        classes = widget.attrs.get('class', '').split()
        classes.append('places')
        return {'class': ' '.join(classes)}

    def compress(self, value_list):
        if value_list:
            return value_list
        return ""


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
