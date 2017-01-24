from django.shortcuts import render, redirect
from models import Users


def index(request):
    print '*'*50
    print "index"
    return render(request, 'login/index.html')


def login(request):
    if request.method == "POST":
        if login.Users.objects.filter(email == request.POST['email']) == "":
            print "NO GOOD!"
        else:
            print login.Users.objects.id.filter(email == request.POST['email'])
    return redirect('/')


def register(request):
    print '*'*50
    print "register"
    return render(request, "login/register.html")


def newReg(request):
    if request.method == "POST":
        if request.POST['password'] == request.POST['password2']:
            Users.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], password=request.POST['password'])
            request.session['userId']= Users.objects.only('id').get(email__contains=request.POST['email']).id
            print request.session['userId']
        else:
                print "NO GOOD!"
        return redirect('/messages/')
