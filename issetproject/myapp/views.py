from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        if 'un' in request.POST: # ISSET CHECK
            name = request.POST['un']
            print('Login form request')

        elif 'contact' in request.POST:
            print('Contact Form Request')

    return render(request,'index.html')
