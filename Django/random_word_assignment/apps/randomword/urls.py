from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),     # This line has changed!
    url(r'^redirect$', views.index)
]