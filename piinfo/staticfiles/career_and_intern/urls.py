from django.contrib import admin
from django.urls import path, include
from career_and_intern import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('career_with_us',views.career_with_us, name = "career_with_us"),  # Career With Us Page
    path('tech_discovery', views.tech_discovery, name="tech_discovery"),
    path('trainee_placement', views.trainee_placement, name = "trainee_placement"),
    path('6weeks_intern', views.six_weeks_intern, name='six_weeks_intern'),
    path('hope_program', views.hope_program, name='hope_program'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
