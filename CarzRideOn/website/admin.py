from django.contrib import admin

from .models import Ratings, Rides, Contactus, UserRides, Users

admin.site.register(Ratings)
admin.site.register(Rides)
admin.site.register(Contactus)
admin.site.register(UserRides)
admin.site.register(Users)
