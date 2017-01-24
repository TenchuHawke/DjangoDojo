from django.shortcuts import render, redirect
from models import Courses
# Create your views here.
def index(request):
    print "*"*50
    context = {
    "courses" : Courses.objects.all(),
    }
    return render(request, 'course/index.html', context)
def addCourse(request):
    if request.method == "POST":
        Courses.objects.create(courseName=request.POST['Name'], courseDesc=request.POST['Description'])
    return redirect('/')

def delete(request, id):
    if request.method == "POST":
        Courses.objects.filter(id=id).delete()
    return redirect('/')
