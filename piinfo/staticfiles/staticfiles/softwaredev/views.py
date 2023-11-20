from django.shortcuts import render
from softwaredev.models import *
# Create your views here.


'''

SOFTWARE DEVELOPMENT

'''
def mobile_applications(request):
    mobile_applications = Mobile_Applications.objects.all()
    return render(request, 'software_development/mobile_applications.html' , {'data' : mobile_applications})

def desktop_applications(request):
    desktop_applications = Desktop_Applications.objects.all()
    return render(request, 'software_development/desktop_applications.html' , {'data' : desktop_applications})

def web_applications(request):
    web_applications = Web_Applications.objects.all()
    return render(request, 'software_development/web_applications.html' , {'data' : web_applications})


