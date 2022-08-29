from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
    path("api/projects/", include("projects.urls")),
    path("api/v2/", include("SoftAPI.routers")),
]
