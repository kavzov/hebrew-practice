from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.random, name='random_time'),
    url(r'^custom/$', views.custom, name='custom_time'),
]
