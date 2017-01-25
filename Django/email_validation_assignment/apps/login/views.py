from django.shortcuts import render, redirect
from django.contrib import messages
from models import Users
import re, bcrypt


def index(request):
    print '*'*50
    print "index"
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        if len(Users.objects.filter(email=request.POST['email']))==1:
            incPassword=request.POST['password']
            storedPassword=Users.objects.only('password').get(email=request.POST['email']).password
            if bcrypt.hashpw(incPassword.encode(), storedPassword.encode())  == storedPassword:
                print "it works"
                messages.info(request, "User Logged in")
                request.session['userId']= Users.objects.only('id').get(email=request.POST['email']).id
                print request.session['userId']
                userName=Users.objects.only('first_name').get(id=request.session['userId']).first_name
                messages.info(request, "Welcome user number "+userName)
                return redirect('/mainpage/')
            else:
                messages.info(request, "The password doesn't match!  Try again!")
                return redirect('/login')
        else:
            print "error!"
            messages.info(request, "The password doesn't match!  Try again!")
    return redirect('/')


def register(request):
    print '*'*50
    print "register"
    return render(request, "login/register.html")


def newReg(request):
    if request.method == "POST":
        if len(Users.objects.filter(email=request.POST['email']))==1:
            messages.info(request, "That user already exists, login on the login page!")
            return redirect('/login')
        if request.POST['password'] == request.POST['password2']:
            password=request.POST['password']
            hashed=bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=hashed)
            UserData=Users.objects.filter(email__contains=request.POST['email'])
            request.session['userId']=UserData['id']
            request.session['userName']=UserData['first_name']
            print request.session['userId']
            print Users.objects.only('password').get(email=request.POST['email']).password
        else:
            print "NO GOOD!"
            messages.info(request, "Passwords don't match, try again!")
            return render(request, "login/register.html")
    return redirect('/login')
