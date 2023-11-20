from django.shortcuts import render, HttpResponse
from portals.models import *

# Create your views here.
def elive_today(request):
    data = Elive_today.objects.all()
    return render(request, 'portals/elive_today.html',{'data':data})

def chandigarh_web(request):
    data = Chandigarh_web.objects.all()
    return render(request, 'portals/chandigarh_web.html',{'data':data})

def class_ikart(request):
    data = Class_ikart.objects.all()
    return render(request, 'portals/class_ikart.html',{'data':data})