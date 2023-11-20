from django.contrib import admin

from .models import *



'''
Services 
'''
class Services_Box_Admin(admin.StackedInline):
    model = Services_box

@admin.register(Services)

class Service_Admin(admin.ModelAdmin):
    inlines = [Services_Box_Admin]

    class Meta:
        model = Services
    
'''
Services 
'''
class Automobile_Box_Admin(admin.StackedInline):
    model = Automobile_Box

@admin.register(Automobile)

class Service_Admin(admin.ModelAdmin):
    inlines = [Automobile_Box_Admin]

    class Meta:
        model = Automobile
    


'''
Education 
'''
class Education_Box_Admin(admin.StackedInline):
    model = Education_Box

@admin.register(Education)

class Education_Admin(admin.ModelAdmin):
    inlines = [Education_Box_Admin]

    class Meta:
        model = Education
    

'''
Tours_travels 
'''
class Tours_Travels_Box_Admin(admin.StackedInline):
    model = Tours_Travels_Box

@admin.register(Tours_Travels)

class Education_Admin(admin.ModelAdmin):
    inlines = [Tours_Travels_Box_Admin]

    class Meta:
        model = Tours_Travels
    
'''
Finance 
'''
class Finance_Box_Admin(admin.StackedInline):
    model = Finance_Box

@admin.register(Finance)

class Finance_Admin(admin.ModelAdmin):
    inlines = [Finance_Box_Admin]

    class Meta:
        model = Finance
    
    
'''
Medical_Healthcare 
'''
class Medical_Healthcare_Box_Admin(admin.StackedInline):
    model = Medical_Healthcare_Box

@admin.register(Medical_Healthcare)

class Medical_Healthcare_Admin(admin.ModelAdmin):
    inlines = [Medical_Healthcare_Box_Admin]

    class Meta:
        model = Medical_Healthcare
    
