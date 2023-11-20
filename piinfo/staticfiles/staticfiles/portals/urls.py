from django.contrib import admin
from django.urls import path, include
from portals import views


urlpatterns = [
    path('elive_today', views.elive_today, name = 'elive_today'),
    path('chandigarh_web', views.chandigarh_web, name = 'chandigarh_web'),
    path('class_ikart', views.class_ikart, name = 'class_ikart'),

]
