from django.shortcuts import render
from web_services.models import *
# Create your views here.


# '''

# WEB SERVICES

# '''


# def graphic_design(request):
#     header = Web_Services_Header.objects.all()
#     graphic_design = Graphic_Design_Card.objects.all()
#     return render(request, 'web_services/graphic_design.html' ,{'data' : graphic_design,
#                                                                'header' : header})

# def web_design(request):
#     header = Web_Services_Header.objects.all()
#     web_design = Web_Design_Card.objects.all()
#     return render(request, 'web_services/web_design.html' , {'data' : web_design,
#                                                             'header' : header})

# def domain_register(request):
#     header = Web_Services_Header.objects.all()
#     domain_register = Domain_Registration_Card.objects.all()
#     return render(request, 'web_services/domain_register.html' , {'data' : domain_register,
#                                                                'header' : header})

# def web_hosting(request):
#     header = Web_Services_Header.objects.all()
#     web_hosting = Web_Hosting_Card.objects.all()
#     return render(request, 'web_services/web_hosting.html' , {'data' : web_hosting,
#                                                                'header' : header})

# def web_marketing(request):
#     header = Web_Services_Header.objects.all()
#     web_marketing = Web_Marketing_Card.objects.all()
#     return render(request, 'web_services/web_marketing.html' , {'data' : web_marketing,
#                                                                'header' : header})






'''
Web Hosting
'''
def web_hosting(request):
    header = Web_Hosting.objects.all()
    box = Web_Hosting_Box.objects.all()
    return render(request, 'web_services/web_hosting.html',{'header':header,'box':box})

def graphic_design(request):
    header = Graphic_Design.objects.all()
    box = Graphic_Design_Box.objects.all()
    return render(request, 'web_services/graphic_design.html',{'header':header,'box':box})

def web_design(request):
    header = Web_Design.objects.all()
    box = Web_Design_Box.objects.all()
    return render(request, 'web_services/web_design.html',{'header':header,'box':box})

def domain_register(request):
    header = Domain_Register.objects.all()
    box = Domain_Register_Box.objects.all()
    return render(request, 'web_services/domain_register.html',{'header':header,'box':box})

def web_marketing(request):
    header = Web_Marketing.objects.all()
    box = Web_Marketing_Box.objects.all()
    return render(request, 'web_services/web_marketing.html',{'header':header,'box':box})