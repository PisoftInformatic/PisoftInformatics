from django.contrib import admin
from .models import *

# Register your models here.

admin.site.site_header = "Pisoft Informatics"
admin.site.site_title = "Admin Panel"
admin.site.index_title = 'Pisoft'


class home_proejct_images(admin.ModelAdmin):
    list_display = ('project_name', 'project_link', 'project_image')
admin.site.register(Homepage_Recent_project_data, home_proejct_images)



'''
PORTFOLIO
'''
class Show_Portfolio_Data(admin.ModelAdmin):
    list_display=  ('device', 'project_link','project_image')
admin.site.register(Portfolio, Show_Portfolio_Data)


'''

GALLERY

'''

class Show_Gallery_Data(admin.ModelAdmin):
    list_display = ('title', 'image')
admin.site.register(Gallery, Show_Gallery_Data)
