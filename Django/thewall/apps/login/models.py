from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.CharField(max_length=60, unique=True)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
