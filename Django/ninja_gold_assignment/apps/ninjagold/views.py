from django.shortcuts import render, HttpResponse, redirect
import random, string

def index(request):
    print "*"*50
    return render(request, 'ninjagold/index.html')
