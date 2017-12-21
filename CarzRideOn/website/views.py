import datetime

from django.shortcuts import render
from .forms import RidesForm, UpdateProfileForm


def index(request):
    return render(request, 'website/index.html', {"temp": "temp"})


def offer_ride(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = RidesForm(request.POST)
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
                form.save()

                return render(request, 'website/index.html', {'temp': 'temp'})

        form = RidesForm()
        return render(request, 'website/offerride.html', {"form": form})
    else:
        return render(request, 'website/index.html', {"temp": "temp"})



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
        return render(request, 'website/update_profile.html', {"form": form})
    else:
        return render(request, 'website/index.html', {"temp": "temp"})
