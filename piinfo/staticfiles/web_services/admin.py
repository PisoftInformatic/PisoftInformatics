from django.contrib import admin
from web_services.models import *
# Register your models here.





'''

WEB SERVICES

'''
# admin.site.register(Web_Services_Header)

# class Show_Graphic_Design_Data(admin.ModelAdmin):
#     list_display = ('heading', 'description')
# admin.site.register(Graphic_Design_Card, Show_Graphic_Design_Data)

# class Show_Web_Design_Data(admin.ModelAdmin):
#     list_display = ('heading', 'description')
# admin.site.register(Web_Design_Card, Show_Web_Design_Data)

# class Show_Web_Hosting_Data(admin.ModelAdmin):
#     list_display = ('heading', 'description')
# admin.site.register(Web_Hosting_Card, Show_Web_Hosting_Data)

# class Show_Web_Marketing_Data(admin.ModelAdmin):
#     list_display = ('heading', 'description')
# admin.site.register(Web_Marketing_Card, Show_Web_Marketing_Data)

# class Show_Domain_Registration_Data(admin.ModelAdmin):
#     list_display = ('heading', 'description')
# admin.site.register(Domain_Registration_Card, Show_Domain_Registration_Data)







'''
Web Hosting
'''
class Web_Hosting_Box_Admin(admin.StackedInline):
    model = Web_Hosting_Box

@admin.register(Web_Hosting)

class Web_Hosting_Box(admin.ModelAdmin):
    inlines = [Web_Hosting_Box_Admin]

    class Meta:
        model = Web_Hosting


'''
Graphic Design 
'''
class Graphic_Design_Box_Admin(admin.StackedInline):
    model = Graphic_Design_Box

@admin.register(Graphic_Design)

class Graphic_Design_Admin(admin.ModelAdmin):
    inlines = [Graphic_Design_Box_Admin]

    class Meta:
        model = Graphic_Design
    

'''
Web Design 
'''
class Web_Design_Box_Admin(admin.StackedInline):
    model = Web_Design_Box

@admin.register(Web_Design)

class Web_Design_Admin(admin.ModelAdmin):
    inlines = [Web_Design_Box_Admin]

    class Meta:
        model = Web_Design
    
'''
Web Marketing 
'''
class Web_Marketing_Box_Admin(admin.StackedInline):
    model = Web_Marketing_Box

@admin.register(Web_Marketing)

class Web_Markewting_Admin(admin.ModelAdmin):
    inlines = [Web_Marketing_Box_Admin]

    class Meta:
        model = Web_Marketing
    
'''
Domain Register 
'''
class Domain_Register_Box_Admin(admin.StackedInline):
    model = Domain_Register_Box

@admin.register(Domain_Register)

class Domain_Register_Admin(admin.ModelAdmin):
    inlines = [Domain_Register_Box_Admin]

    class Meta:
        model = Domain_Register
    