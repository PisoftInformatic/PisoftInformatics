from django.contrib import admin
from django.urls import path, include
from records import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   path('henquiry', views.henquiry, name='henquiry'), # HOPE Enquery Page
    path('apply_job', views.apply_job, name = 'apply_job'),  # apply job page
    path('contact', views.contact, name = 'contact'),  
    path('registration', views.registration, name='registration'),
    path('free_demo', views.free_demo, name='free_demo'),
    path('module', views.module, name='module'),

]