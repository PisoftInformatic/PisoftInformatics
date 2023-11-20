from django.contrib import admin
from softwaredev.models import *
# Register your models here.




'''

SOFTWARE DEVELOPMENT

'''
class Show_Mobile_Applications_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Mobile_Applications, Show_Mobile_Applications_Data)

class Show_Desktop_Applications_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Desktop_Applications, Show_Desktop_Applications_Data)

class Show_Web_Applications_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Web_Applications, Show_Web_Applications_Data)