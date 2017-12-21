from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^offerrides/$', views.offer_ride, name="offer_ride"),
    url(r'^profile/$', views.view_profile, name="view_profile"),
    url(r'^update_profile/$', views.update_profile, name="update_profile"),
]