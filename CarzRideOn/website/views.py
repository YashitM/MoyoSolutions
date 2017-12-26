import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from places.forms import PlacesField

from website.models import Rides, UserRides
from .forms import RidesForm, UpdateProfileForm, SearchRideForm, RequestRideForm


def index(request):
    return render(request, 'website/index.html', {"temp": "temp"})


def offer_ride(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all().exists():
            if request.method == 'POST':
                form = RidesForm(request.POST)
                form_source = PlacesField(request.POST)
                if form.is_valid():
                    print("Form Validated")
                    ride = form.save(commit=False)
                    car_model = form.cleaned_data['car_model']
                    seats = form.cleaned_data['seats']
                    seats_available = form.cleaned_data['seats_available']
                    cost = form.cleaned_data['cost']
                    start_time = form.cleaned_data['start_time']
                    message = form.cleaned_data['message']
                    dateofride = form.cleaned_data['dateofride']
                    source_location = form.cleaned_data['source_location']
                    destination_location = form.cleaned_data['destination_location']
                    lat_sou = form.cleaned_data['sou_lati']
                    lat_des = form.cleaned_data['des_lati']
                    lon_sou = form.cleaned_data['sou_long']
                    lon_des = form.cleaned_data['des_long']

                    ride.car_model = car_model
                    ride.fb_id = request.user.customuser_set.all()[0].fb_id
                    ride.seats = seats
                    ride.seats_available = seats_available
                    ride.cost = cost
                    ride.start_time = start_time
                    ride.message = message
                    ride.ridecancelstatus = 0
                    ride.created_at = datetime.datetime.now()
                    ride.dateofride = dateofride
                    ride.source = source_location
                    ride.destination = destination_location
                    ride.destination_latitude = lat_des
                    ride.destination_longitude = lon_des
                    ride.source_latitude = lat_sou
                    ride.source_longitude = lon_sou
                    form.save()

                    return render(request, 'website/index.html', {'temp': 'temp'})
        else:
            return update_profile(request)

        form = RidesForm()
        form_source = PlacesField()
        return render(request, 'website/offerride.html', {"form": form, "form_source": form_source})
    else:
        return render(request, 'website/index.html', {"temp": "temp"})


def view_profile(request):
    if request.user.is_authenticated():
        if request.user.customuser_set.all().exists():
            return render(request, 'website/profile.html', {"update_profile": "True"})
        return render(request, 'website/profile.html', {"update_profile": "False"})
    return render(request, 'website/index.html', {"temp": "temp"})


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
        return render(request, 'website/update_profile.html', {"form": form})
    else:
        return render(request, 'website/index.html', {"temp": "temp"})


def take_ride(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all().exists():
            if request.method == 'POST':
                form = SearchRideForm(request.POST)
                if form.is_valid():
                    source_location = form.cleaned_data['source_location']
                    destination_location = form.cleaned_data['destination_location']
                    lat_sou = form.cleaned_data['sou_lati']
                    lat_des = form.cleaned_data['des_lati']
                    lon_sou = form.cleaned_data['sou_long']
                    lon_des = form.cleaned_data['des_long']

                    user_id = request.user.customuser_set.all()[0].fb_id
                    available_rides = Rides.objects.exclude(
                        fb_id=user_id
                    )
                    available_rides_owners = []
                    users = User.objects.all()
                    for ride in available_rides:
                        user_id = ride.fb_id
                        for user in users:
                            if user.socialaccount_set.all().exists():
                                if user.socialaccount_set.all()[0].uid == user_id:
                                    available_rides_owners.append(user.socialaccount_set.all()[0].extra_data['name'])
                    context = {"s_location": source_location, "s_lat": lat_sou, "s_lon": lon_sou,
                               "d_location": destination_location, "d_lat": lat_des, "d_lon": lon_des,
                               'available_rides': available_rides, 'owners': available_rides_owners}

                    return render(request, 'website/searchride.html', context)

            form = SearchRideForm()
            return render(request, 'website/takeride.html', {"form": form})
        else:
            return update_profile(request)

    else:
        return render(request, 'website/index.html', {"temp": "temp"})


def request_ride(request, ride_id):
    if request.user.is_authenticated:
        if request.user.customuser_set.all().exists():
            if request.method == 'POST':
                form = RequestRideForm(request.POST)
                if form.is_valid():
                    ride_request = form.save(commit=False)
                    ride_request.fb_id = request.user.socialaccount_set.all()[0].uid
                    ride_request.task_id = ride_id
                    ride_request.status = "1"
                    ride_request.created_at = datetime.datetime.now()
                    ride_request.message = form.cleaned_data['message']

                    form.save()
                    return render(request, 'website/index.html', {"temp": "temp"})

            selected_ride = Rides.objects.get(pk=ride_id)
            users = User.objects.all()
            selected_ride_owner = ""
            for user in users:
                if user.socialaccount_set.all().exists():
                    if user.socialaccount_set.all()[0].uid == selected_ride.fb_id:
                        selected_ride_owner = user.socialaccount_set.all()[0].extra_data['name']
            form = RequestRideForm({'ride_id': str(ride_id)})
            return render(request, 'website/request_ride.html', {"form": form, 'selected_ride': selected_ride, 'selected_ride_owner': selected_ride_owner})
        else:
            return update_profile(request)

    else:
        return render(request, 'website/index.html', {"temp": "temp"})


