from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^', include('apps.login.urls', namespace="main")),
    url(r'^login', include('apps.mainpage.urls', namespace="login")),
]
