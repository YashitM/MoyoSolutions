import datetime

import requests
from allauth.socialaccount.models import SocialToken
from django.shortcuts import render
from .forms import RidesForm, UpdateProfileForm
from .forms import PlacesField as PlacesFieldForm


def index(request):
    return render(request, 'website/index.html', {"temp": "temp"})


def offer_ride(request):
    if request.method == 'POST':
        form = RidesForm(request.POST)
        form_location_source = PlacesFieldForm(request.POST)
        form_location_destination = PlacesFieldForm(request.POST)
        if form.is_valid():
            ride = form.save(commit=False)
            car_model = form.cleaned_data['car_model']
            seats = form.cleaned_data['seats']
            seats_available = form.cleaned_data['seats_available']
            cost = form.cleaned_data['cost']
            dateofride = form.cleaned_data['dateofride']
            starttime = form.cleaned_data['start_time']

            ride.start_time = starttime
            ride.dateofride = dateofride
            ride.cost = cost
            ride.seats_available = seats_available
            ride.seats = seats
            ride.car_model = car_model
            ride.created_at = datetime.datetime.now()
            ride.ridecancelstatus = False

            # source_place = form_location_source.['place']
            # source_latitude = form_location_source.['Latitude']
            # source_longitude = form_location_source.cleaned_data['Longitude']


            form.save()

            return render(request, 'website/index.html', {'temp': 'temp'})
    else:
        form = RidesForm()
        form_location_source = PlacesFieldForm(request.POST)

    return render(request, 'website/offerride.html', {'form_ride': form, 'form_location': form_location_source})


def view_profile(request):
    if request.user.is_authenticated():
        extra_json = request.user.socialaccount_set.all()
        print(extra_json[0].uid)
    return render(request, 'website/profile.html', {"temp": "temp"})


def update_profile(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST)
            if form.is_valid():
                custom_user = form.save(commit=False)
                gender = form.cleaned_data['gender']
                dob = form.cleaned_data['dob']
                mobile = form.cleaned_data['mobile']
                company = form.cleaned_data['company']
                ref_number = form.cleaned_data['ref_number']
                aadhar = form.cleaned_data['aadhar']

                custom_user.fb_id = request.user.socialaccount_set.all()[0].uid
                custom_user.name = request.user.socialaccount_set.all()[0].extra_data['name']
                custom_user.email = request.user.socialaccount_set.all()[0].extra_data['email']
                custom_user.gender = gender
                custom_user.dob = dob
                custom_user.mobile = mobile
                custom_user.company = company
                custom_user.ref_number = ref_number
                custom_user.created_at = datetime.datetime.now()
                custom_user.aadhar = aadhar
                custom_user.user_id = request.user.id
                custom_user.ref_status = "0"
                form.save()

                return render(request, 'website/index.html', {'temp': 'temp'})

        form = UpdateProfileForm()
        print(request.user.socialaccount_set.all()[0].extra_data['name'])
        return render(request, 'website/update_profile.html', {"form": form})
    else:
        return render(request, 'website/index.html', {"temp": "temp"})
