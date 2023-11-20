from django.contrib import admin
from django.urls import path, include
from erp_solutions import views


from django.conf import settings
from django.conf.urls.static import static


app_name = 'erp_solutions'

urlpatterns = [
   path('education/', views.education, name='education'),
   path('finance/', views.finance, name='finance'),
   path('automobile/', views.automobile, name='automobile'),
   path('medical_and_healthcare/', views.medical_healthcare, name='medical_and_healthcare'),
   path('services/', views.services, name='services'),
   path('tours_and_travels/', views.tours_travels, name='tours_and_travels'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)