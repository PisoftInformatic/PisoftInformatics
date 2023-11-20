from django.contrib import admin
from portals.models import *
# Register your models here.



class Show_ikart_data(admin.ModelAdmin):
    list_display = ('title_of_this_page' , 'page_description', 'website_domain_link')
admin.site.register(Class_ikart, Show_ikart_data)

class Show_Chandigarh_web_data(admin.ModelAdmin):
    list_display = ('title_of_this_page' , 'page_description', 'website_domain_link')
admin.site.register(Chandigarh_web, Show_Chandigarh_web_data)

class Show_Elive_today_data(admin.ModelAdmin):
    list_display = ('title_of_this_page' , 'page_description', 'website_domain_link')
admin.site.register(Elive_today, Show_Elive_today_data)


