import datetime

from django.contrib.auth.models import User
from django.shortcuts import render
from website.models import Rides, UserRides, CustomUser
from .forms import RidesForm, UpdateProfileForm, SearchRideForm, RequestRideForm, ValidateRequestForm, ContactForm

from fcm_django.models import FCMDevice


def index(request):
    return render(request, 'website/index.html', {"custom_notifications": ""})


def offer_ride(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
            if request.method == 'POST':
                form = RidesForm(request.POST)
                if form.is_valid():
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

                    return render(request, 'website/index.html', {'custom_notifications': 'Ride has been created!'})
        else:
            return update_profile(request)

        form = RidesForm()
        return render(request, 'website/offerride.html', {"form": form})
    else:
        return render(request, 'website/index.html', {"custom_notifications": ""})


def view_profile(request):
    if request.user.is_authenticated():
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
            time = datetime.datetime.now().time()
            return render(request, 'website/profile.html', {"update_profile": "True", "current_time": time})
        time = datetime.datetime.now().time()
        return render(request, 'website/profile.html', {"update_profile": "False", "current_time": time})
    return render(request, 'website/index.html', {"custom_notifications": ""})


def update_profile(request):
    if request.user.is_authenticated:
        if not request.user.customuser_set.all()[0].mobile and not request.user.customuser_set.all()[0].fcm_id:
            if request.method == 'POST':
                form = UpdateProfileForm(request.POST)
                if form.is_valid():
                    custom_user = CustomUser.objects.get(user_id=request.user.id)
                    gender = form.cleaned_data['gender']
                    dob = form.cleaned_data['dob']
                    mobile = form.cleaned_data['mobile']
                    company = form.cleaned_data['company']
                    ref_number = form.cleaned_data['ref_number']
                    aadhar = form.cleaned_data['aadhar']
                    fcm_id = form.cleaned_data['fcm_id']

                    if "+91" in ref_number:
                        ref_number = ref_number.replace("+91", "")

                    custom_user.gender = gender
                    custom_user.dob = dob
                    custom_user.mobile = mobile
                    custom_user.company = company
                    custom_user.ref_number = ref_number
                    custom_user.aadhar = aadhar
                    custom_user.ref_status = "0"
                    custom_user.fcm_id = fcm_id

                    new_device = FCMDevice()
                    new_device.registration_id = fcm_id
                    new_device.type = "web"
                    new_device.user_id = request.user.id
                    new_device.save()

                    custom_user.save()
                    if ref_number:
                        for user in CustomUser.objects.all():
                            if user.mobile:
                                if user.mobile == ref_number and user.mobile != mobile:
                                    if user.fcm_id:
                                        device = FCMDevice.objects.get(user_id=user.user_id)
                                        device.send_message("Title", "You have a new Referral, Please check and confirm.")
                                        break
                    return render(request, 'website/index.html', {'custom_notifications': 'Profile has been updated!'})

            form = UpdateProfileForm()
            return render(request, 'website/update_profile.html', {"form": form})
        else:
            return render(request, 'website/index.html', {'custom_notifications': 'Profile has already been updated'})
    else:
        return render(request, 'website/index.html', {"custom_notifications": ""})


def take_ride(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
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
        return render(request, 'website/index.html', {"custom_notifications": "Not Logged In :("})


def request_ride(request, ride_id):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
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
                    return render(request, 'website/index.html', {"custom_notifications": "Ride Request Sent!"})

            selected_ride = Rides.objects.get(pk=ride_id)
            users = User.objects.all()
            selected_ride_owner = ""
            for user in users:
                if user.socialaccount_set.all().exists():
                    if user.socialaccount_set.all()[0].uid == selected_ride.fb_id:
                        selected_ride_owner = user.socialaccount_set.all()[0].extra_data['name']
            form = RequestRideForm()
            return render(request, 'website/request_ride.html',
                          {"form": form, 'selected_ride': selected_ride, 'selected_ride_owner': selected_ride_owner})
        else:
            return update_profile(request)

    else:
        return render(request, 'website/index.html', {"custom_notifications": "Not Logged In :("})


def view_requests(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
            all_rides = Rides.objects.filter(fb_id=request.user.socialaccount_set.all()[0].uid)
            all_rides_id = []
            for ride in all_rides:
                all_rides_id.append(ride.id)
            all_ride_requests = UserRides.objects.all()
            filtered_ride_requests = []
            for ride_request in all_ride_requests:
                if ride_request.id in all_rides_id and ride_request.status == "1":
                    filtered_ride_requests.append(ride_request)
            if filtered_ride_requests:
                return render(request, 'website/view_request.html', {'requests': filtered_ride_requests})
            else:
                return render(request, 'website/index.html', {"custom_notifications": "No Pending Requests."})
        else:
            return update_profile(request)
    else:
        return render(request, 'website/index.html', {"custom_notifications": "Not Logged In :("})


def get_user_from_request(selected_request):
    users = User.objects.all()
    for user in users:
        if user.socialaccount_set.all().exists():
            if user.socialaccount_set.all()[0].uid == selected_request.fb_id:
                return user.socialaccount_set.all()[0].extra_data['email']
    return None


def validate_ride_request(request, request_id):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
            if request.method == 'POST':
                form = ValidateRequestForm(request.POST)
                if form.is_valid():
                    ride_request = UserRides.objects.get(pk=request_id)
                    ride_request.status = form.cleaned_data['validation'][0]
                    if ride_request.status == "2":
                        user_email = get_user_from_request(ride_request)
                        # devices = FCMDevice.objects.get(registration_id=request.user.customuser_set)
                        # devices.send_message("Happy name day!")
                        print("Sent to " + user_email)
                    ride_request.save()
                    return view_requests(request)

            form = ValidateRequestForm()
            selected_request = UserRides.objects.get(pk=request_id)
            users = User.objects.all()
            request_owner = ""
            for user in users:
                if user.socialaccount_set.all().exists():
                    if user.socialaccount_set.all()[0].uid == selected_request.fb_id:
                        request_owner = user.socialaccount_set.all()[0].extra_data['name']
            return render(request, 'website/validate_request.html',
                          {'request': selected_request, 'request_owner': request_owner, 'form': form})
        else:
            return update_profile(request)
    else:
        return render(request, 'website/index.html', {"custom_notifications": "Not Logged In :("})


def contact_us(request):
    if request.user.is_authenticated:
        if request.user.customuser_set.all()[0].mobile and request.user.customuser_set.all()[0].aadhar:
            if request.method == 'POST':
                form = ContactForm(request.POST)
                if form.is_valid():
                    contact = form.save(commit=False)
                    contact.fb_id = request.user.customuser_set.all()[0].fb_id
                    contact.type = form.cleaned_data['type']
                    contact.message = form.cleaned_data['message']
                    contact.attachment_url = form.cleaned_data['image_url']
                    contact.save()

                    return render(request, 'website/index.html', {"custom_notifications": "Message has been sent!"})
            form = ContactForm()
            for i in form:
                print(i.name)
            return render(request, 'website/contact_us.html', {'form': form})
        else:
            return update_profile(request)
    else:
        return render(request, 'website/index.html', {"custom_notifications": "Not Logged In :("})
