import datetime
from django import forms
from .models import Rides, CustomUser, UserRides, Contactus


class RidesForm(forms.ModelForm):
    car_model = forms.CharField(max_length=100)
    seats = forms.CharField(max_length=10)
    seats_available = forms.IntegerField()
    cost = forms.CharField(max_length=10)
    start_time = forms.CharField(max_length=100)
    dateofride = forms.CharField(max_length=100)
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
    fcm_id = forms.CharField(max_length=1000)

    class Meta:
        model = CustomUser
        fields = ['gender', 'dob', 'mobile', 'company', 'ref_number', 'aadhar', 'fcm_id',]


class SearchRideForm(forms.Form):
    source_location = forms.CharField(max_length=1000)
    sou_lati = forms.CharField(max_length=1000)
    sou_long = forms.CharField(max_length=1000)
    des_lati = forms.CharField(max_length=1000)
    des_long = forms.CharField(max_length=1000)
    destination_location = forms.CharField(max_length=1000)


class RequestRideForm(forms.ModelForm):
    message = forms.TextInput()

    class Meta:
        model = UserRides
        fields = ['message', ]


VALIDATE_REQUEST_CHOICES = (
    ('2', 'Accept'),
    ('3', 'Reject'),
)


class ValidateRequestForm(forms.Form):
    validation = forms.MultipleChoiceField(
        required=False,
        widget=forms.CheckboxSelectMultiple,
        choices=VALIDATE_REQUEST_CHOICES,
    )


MESSAGE_TYPE_CHOICES = (
    ('Complaint', 'Complaint'),
    ('Query', 'Query'),
    ('Feedback', 'Feedback'),
)


class ContactForm(forms.ModelForm):
    type = forms.ChoiceField(
        required=True,
        widget=forms.Select(),
        choices=MESSAGE_TYPE_CHOICES,
    )
    image_url = forms.CharField(max_length=1000)
    message = forms.TextInput()

    class Meta:
        model = Contactus
        fields = ['type', 'message', 'image_url', ]