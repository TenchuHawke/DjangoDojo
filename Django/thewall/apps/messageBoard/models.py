from __future__ import unicode_literals

from django.db import models


class Messages(models.Model):
    message = models.TextField()
    userId = models.ForeignKey('login.Users', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comments(models.Model):
        Comment = models.TextField()
        userId = models.ForeignKey('login.Users', on_delete=models.CASCADE)
        messageId = models.ForeignKey('Messages', on_delete=models.CASCADE)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)
