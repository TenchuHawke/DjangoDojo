from django.conf.urls import url
from . import views

urlpatterns = [
   # This line has changed!
    url(r'login$', views.login),
    url(r'register$', views.register),
    url(r'newReg$', views.newReg),
    url(r'^$', views.index),
]
