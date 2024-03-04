from django.contrib import admin
from records.models import *
# Register your models here.


# class Show_henquiry_data(admin.ModelAdmin):
#     list_filter = ('intrested_in', 'education','collage')
#     list_display = ('name', 'phone','email','intrested_in','education','collage')
# admin.site.register(HEnquiry, Show_henquiry_data)


class Show_Apply_Job_Data(admin.ModelAdmin):
    search_fields = ('full_name', 'phone_number')
    list_filter = ('position_applied_for', 'qualification')
    list_display = ('full_name', 'phone_number','email', 'position_applied_for','qualification')
admin.site.register(Apply_Job, Show_Apply_Job_Data)


class Show_contact_Data(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ('name', 'email','subject')
admin.site.register(Contact_data, Show_contact_Data)


class Show_Registrations_Data(admin.ModelAdmin):
    search_fields = ['name','module', 'date']
    list_filter = ('module', 'training_program')
    list_display = ('name','email', 'phone', 'module','training_program', 'payment_method', 'date')
admin.site.register(Registration,Show_Registrations_Data)



# Intrested In Free Demo
class Free_Demo(admin.ModelAdmin):
    list_display = ('company_name', 'phone', 'email', 'module', 'header_ids')
admin.site.register(Demo_Data, Free_Demo)

