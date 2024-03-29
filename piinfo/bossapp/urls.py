from django.contrib import admin
from django.urls import path
from bossapp import views

from django.conf import settings
from django.conf.urls.static import static

app_name = 'bossapp'



urlpatterns = [
    path('', views.index, name = 'index'),  # home page
    path('gallery', views.gallery, name='gallery'), # Gallery Page
    path('portfolio', views.portfolio, name='portfolio'),
    path('registration', views.registration, name='registration'),
    path('rough', views.rough, name="rough"),
    path('training', views.training, name="training"),


]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
