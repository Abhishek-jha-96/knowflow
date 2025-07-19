from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView
)


urlpatterns_v1 = [
    path(
        "api/v1/",
        include("apps.user.urls"),
    ),
    path(
        "api/v1/",
        include("apps.conversation.urls"),
    )
]
urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/schema/v1/",
        SpectacularAPIView.as_view(api_version="v1", patterns=urlpatterns_v1),
        name="schema-v1",
    ),
    path(
        "api/v1/docs/",
        SpectacularSwaggerView.as_view(url_name="schema-v1"),
        name="swagger-ui-v1",
    ),
]

urlpatterns += urlpatterns_v1
