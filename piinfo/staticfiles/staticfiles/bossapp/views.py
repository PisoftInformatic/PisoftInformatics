from django.shortcuts import render, HttpResponse, redirect
from .models import *
from records.models import Contact_data

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import messages

# Create your views here.
def index(request):
    project_data = Homepage_Recent_project_data.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        save_data = Contact_data(name = name, phone=phone, email=email,
                                  subject=subject, message=message)
        save_data.save()
        messages.success(request, "We Will Contact You Soon.......")
    return render(request, 'index.html', {'data':project_data})

def portfolio(request):
    data = Portfolio.objects.all()
    return render(request, 'portfolio.html', {'data':data})

def registration(request):
    return render(request, 'registration.html')

def rough(request):
    return render(request, 'rough.html')





'''
Gallery 
'''


def gallery(request):
    images = Gallery.objects.all()

    return render(request,'gallery.html', {'images':images})
    # return render(request, 'gallery.html')

def training(request):
    return render(request, 'training.html')