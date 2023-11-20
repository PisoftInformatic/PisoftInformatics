from django.shortcuts import render
from web_services.models import *
# Create your views here.


# '''

# WEB SERVICES

# '''


def graphic_design(request):
    header = Web_Services_Header.objects.all()
    graphic_design = Graphic_Design_Card.objects.all()
    return render(request, 'web_services/graphic_design.html' ,{'data' : graphic_design,
                                                               'header' : header})

def web_design(request):
    header = Web_Services_Header.objects.all()
    web_design = Web_Design_Card.objects.all()
    return render(request, 'web_services/web_design.html' , {'data' : web_design,
                                                            'header' : header})

def domain_register(request):
    header = Web_Services_Header.objects.all()
    domain_register = Domain_Registration_Card.objects.all()
    return render(request, 'web_services/domain_register.html' , {'data' : domain_register,
                                                               'header' : header})

def web_hosting(request):
    header = Web_Services_Header.objects.all()
    web_hosting = Web_Hosting_Card.objects.all()
    return render(request, 'web_services/web_hosting.html' , {'data' : web_hosting,
                                                               'header' : header})

def web_marketing(request):
    header = Web_Services_Header.objects.all()
    web_marketing = Web_Marketing_Card.objects.all()
    return render(request, 'web_services/web_marketing.html' , {'data' : web_marketing,
                                                               'header' : header})


