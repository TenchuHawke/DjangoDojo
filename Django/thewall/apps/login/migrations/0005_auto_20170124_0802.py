# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=60, unique=True),
        ),
    ]