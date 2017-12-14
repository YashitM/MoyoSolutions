from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name="index_page"),
    url(r'^login/$', views.login, name="login_page"),
    url(r'^signup/$', views.signup, name="signup_page"),
    url(r'^offerrides/$', views.offer_ride, name="offer_ride"),
]