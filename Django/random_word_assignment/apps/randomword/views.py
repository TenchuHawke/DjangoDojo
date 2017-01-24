from django.shortcuts import render, HttpResponse, redirect
import random, string

def index(request):

    print "*"*50

    try:
        request.session['count']=request.session['count']+1
        count=request.session['count']
        print "incrementing"
        if count>15:
            del request.session['count']
    except KeyError:
        request.session['count']=1
        count=request.session['count']
        print "setting"
    output = ""
    # for i in range (1, 16):
    output += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(15))
    print output
    print count
    context = {
        "string": output,
        }
    print "*"*50
    return render(request, 'randomword\index.html', context)
