from django.shortcuts import render

def index(request):
    print '*'*50
    print "index"
    return render(request, 'mainpage/index.html')
