from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^offerrides/$', views.offer_ride, name="offer_ride"),
    url(r'^takerides/$', views.take_ride, name="take_ride"),
    url(r'^view_requests/$', views.view_requests, name="view_requests"),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    url(r'^update_profile/$', views.update_profile, name="update_profile"),
    url(r'^request_ride/(?P<ride_id>\d+)/$', views.request_ride, name="request_ride"),
    url(r'^contact_us/$', views.contact_us, name="contact_us"),
    url(r'^validate_request/(?P<request_id>\d+)/$', views.validate_ride_request, name="validate_ride_request"),
    url(r'^view_rides/$', views.view_user_rides, name="view_user_rides"),
    url(r'^cancel_ride/(?P<ride_id>\d+)/$', views.cancel_ride, name="cancel_ride"),
    url(r'^edit_ride/(?P<ride_id>\d+)/$', views.edit_rides, name="edit_ride"),
]