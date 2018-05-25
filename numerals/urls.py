from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.random, name='random_number'),
    url(r'^custom/$', views.custom, name='custom_number'),
]
