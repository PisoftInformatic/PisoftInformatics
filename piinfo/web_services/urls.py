from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from web_services import views

urlpatterns = [
    path('graphic_design', views.graphic_design, name='graphic_design'),
    path('web_design', views.web_design, name='web_design'),
    path('domain_register', views.domain_register, name='domain_register'),
    path('web_hosting', views.web_hosting, name='web_hosting'),
    path('web_marketing', views.web_marketing, name='web_marketing'),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
