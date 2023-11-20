from django.contrib import admin
from django.urls import path
from softwaredev import views

from django.conf import settings
from django.conf.urls.static import static
    



urlpatterns = [
    path('web_applications', views.web_applications, name="web_applications"),
    path('desktop_applications', views.desktop_applications, name="desktop_applications"),
    path('mobile_applications', views.mobile_applications, name="mobile_applications"),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)