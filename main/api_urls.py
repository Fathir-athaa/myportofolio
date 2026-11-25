from django.urls import path
from rest_framework.authtoken import views as authtoken_views

from main import api_views

app_name = "api"

urlpatterns = [
    # Auth token (Tutorial 10)
    path("auth/token/", authtoken_views.obtain_auth_token, name="api_token_auth"),
    path("auth/logout/", api_views.api_logout, name="api_logout"),

    # Project (Tutorial 10)
    path("projects/", api_views.project_list, name="project-list"),
    path("projects/<uuid:id>/", api_views.project_detail, name="project-detail"),

    # Experience
    path("experiences/", api_views.experience_list, name="experience-list"),
    path("experiences/<uuid:experience_id>/", api_views.experience_detail, name="experience-detail"),
    path("experiences/<uuid:experience_id>/star/", api_views.experience_star, name="experience-star"),

    # Organization
    path("organizations/", api_views.organization_list, name="organization-list"),
    path("organizations/<int:organization_id>/", api_views.organization_detail, name="organization-detail"),
    path("organizations/<int:organization_id>/star/", api_views.organization_star, name="organization-star"),
]