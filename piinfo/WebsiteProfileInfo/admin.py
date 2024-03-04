from django.contrib import admin
from WebsiteProfileInfo.models import *

class Show_WebsiteProfileData(admin.ModelAdmin):
    list_display = ('phone','email', 'company_address')
admin.site.register(WebsiteProfileData, Show_WebsiteProfileData)


class Show_SocialProfileLinks(admin.ModelAdmin):
    list_display = ('facebook_link','linkedin_link', 'twitter_link')
admin.site.register(SocialProfileLink, Show_SocialProfileLinks)

