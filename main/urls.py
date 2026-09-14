from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from main.views import show_main, show_experience, show_organization

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("organization/", show_organization, name="show_organization"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)