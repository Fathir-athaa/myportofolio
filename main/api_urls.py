from django.urls import path

from main import api_views

app_name = "api"

urlpatterns = [
    # Experience
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),

    # Organization
    path("organizations/", api_views.organization_list, name="organization-list"),
    path("organizations/<int:organization_id>/", api_views.organization_detail, name="organization-detail"),
    path("organizations/<int:organization_id>/star/", api_views.organization_star, name="organization-star"),
]