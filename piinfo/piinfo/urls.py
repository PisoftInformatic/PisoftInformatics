from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
       
    path('', include('bossapp.urls')),
    path('softwaredev/', include('softwaredev.urls')),
    path('portals/', include('portals.urls')),
    path('erp_solutions/', include('erp_solutions.urls')),
    path('career_and_intern/', include('career_and_intern.urls')),
    path('records/', include('records.urls')),
    path('web_services/', include('web_services.urls')),

]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += staticfiles_urlpatterns()
