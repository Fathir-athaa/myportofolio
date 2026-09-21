from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from main.views import show_main, show_experience, show_organization, add_experience, edit_experience, add_organization, edit_organization, get_experience_json, get_experience_xml, get_organization_json, get_organization_xml, delete_experience, delete_organization

app_name = "main"

urlpatterns = [
    path("", show_main, name="show_main"),
    path("experience/", show_experience, name="show_experience"),
    path("experience/add/", add_experience, name="add_experience"),
    path("experience/<uuid:experience_id>/edit/", edit_experience, name="edit_experience"),
    path("organization/", show_organization, name="show_organization"),
    path("organization/add/", add_organization, name="add_organization"),
    path("organization/<int:organization_id>/edit/", edit_organization, name="edit_organization"),

    # Data delivery
    path("api/experience/", get_experience_json, name="get_experience_json"),
    path("api/experience/xml/", get_experience_xml, name="get_experience_xml"),
    path("api/organization/", get_organization_json, name="get_organization_json"),
    path("api/organization/xml/", get_organization_xml, name="get_organization_xml"),

    # Delete
    path("experience/<uuid:experience_id>/delete/", delete_experience, name="delete_experience"),
    path("organization/<int:organization_id>/delete/", delete_organization, name="delete_organization"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)