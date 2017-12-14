import datetime
from django.shortcuts import render
from .forms import RidesForm
from .forms import PlacesField as PlacesFieldForm


def login(request):
    return render(request, 'website/login.html', {"temp": "temp"})


def index(request):
    return render(request, 'website/index.html', {"temp": "temp"})


def signup(request):
    return render(request, 'website/login.html', {"temp": "temp"})


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
