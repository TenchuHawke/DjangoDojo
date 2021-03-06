# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 05:40
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users')),
            ],
        ),
        migrations.AddField(
            model_name='comments',
            name='messageId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='messageBoard.Messages'),
        ),
        migrations.AddField(
            model_name='comments',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='login.Users'),
        ),
    ]
