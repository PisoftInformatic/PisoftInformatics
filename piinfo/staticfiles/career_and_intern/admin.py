from django.contrib import admin
from career_and_intern.models import *
# Register your models here.




class Show_data(admin.ModelAdmin):
    list_display = ('job_title', 'job_profile', 'job_description', 'city_location', 'experience_required_in_years')
admin.site.register(Career_With_Us, Show_data)


class Show_Tech_Discovery_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Tech_Descovery, Show_Tech_Discovery_Data)


class Show_Six_Months_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Six_Weeks_Intern, Show_Six_Months_Data)


class Show_Hope_Data(admin.ModelAdmin):
    list_display = ('heading', 'description')
admin.site.register(Hope_Program, Show_Hope_Data)

class Show_Trainee_Placement_Data(admin.ModelAdmin):
    list_display = ('trainee_name', 'trainee_placed_company')
admin.site.register(Traniee_with_us, Show_Trainee_Placement_Data)