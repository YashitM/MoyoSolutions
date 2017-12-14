import datetime
from django import forms
from places import Places
from places.widgets import PlacesWidget

from .models import Rides, DestinationLocation


class RidesForm(forms.ModelForm):
    car_model = forms.CharField()
    seats = forms.CharField()
    seats_available = forms.IntegerField()
    cost = forms.CharField(max_length=10)
    dateofride = forms.CharField(max_length=20)
    start_time = forms.CharField(max_length=100)
    message = forms.TextInput()

    class Meta:
        model = Rides
        fields = ['car_model', 'seats', 'seats_available', 'cost', 'dateofride', 'start_time', 'message', ]


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
