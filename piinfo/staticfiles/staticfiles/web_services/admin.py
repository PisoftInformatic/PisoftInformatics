from django.contrib import admin
from web_services.models import *
# Register your models here.





'''

WEB SERVICES

'''
admin.site.register(Web_Services_Header)

class Show_Graphic_Design_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Graphic_Design_Card, Show_Graphic_Design_Data)

class Show_Web_Design_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Web_Design_Card, Show_Web_Design_Data)

class Show_Web_Hosting_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Web_Hosting_Card, Show_Web_Hosting_Data)

class Show_Web_Marketing_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Web_Marketing_Card, Show_Web_Marketing_Data)

class Show_Domain_Registration_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Domain_Registration_Card, Show_Domain_Registration_Data)
