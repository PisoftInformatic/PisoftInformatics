from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Pisoft Informatics"
admin.site.site_title = "Admin Panel"
admin.site.index_title = 'Pisoft'




'''
PORTFOLIO
'''
class Show_Portfolio_Data(admin.ModelAdmin):
    list_display=  ('project_name','device', 'project_link','project_image')
admin.site.register(Portfolio, Show_Portfolio_Data)


'''

GALLERY

'''

class Show_Gallery_Data(admin.ModelAdmin):
    list_display = ('title', 'image')
admin.site.register(Gallery, Show_Gallery_Data)

