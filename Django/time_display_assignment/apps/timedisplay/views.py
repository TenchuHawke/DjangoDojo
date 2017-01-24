import datetime

from django.shortcuts import render, HttpResponse


def index(request):
    print "*"*50
    context = {
        "date": datetime.datetime.now(),
        }
    return render(request, 'timedisplay/index.html', context)
