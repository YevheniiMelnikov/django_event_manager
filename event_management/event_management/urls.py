from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework.permissions import IsAuthenticated

api_info = openapi.Info(title="Admin Rest", default_version="0.1")
schema_view = get_schema_view(
    api_info, public=True, url="", permission_classes=[IsAuthenticated]
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("events.urls")),
    path("auth/", include("djoser.urls")),
    path("auth/", include("djoser.urls.authtoken")),
    path("auth/", include("djoser.urls.jwt")),
    path("docs/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger"),
]
