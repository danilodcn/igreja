from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.utils.translation import gettext_lazy as _
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from apps.core.views import home

CONFIG_URLS = [
    path("admin/", admin.site.urls),
    path(
        "api-auth/", include("rest_framework.urls", namespace="rest_framework")
    ),
    path(r"?P<ckeditor/", include("ckeditor_uploader.urls")),
    path("doc/", include("django.contrib.admindocs.urls")),
    path(
        "api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"
    ),
    path(
        "api/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"
    ),
]
if settings.DEBUG:
    CONFIG_URLS += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )

APPS_URLS = [
    path("accounts/", include("apps.account.urls")),
    path("api/", include("apps.api.urls")),
    path("api/blog/", include("apps.blog.urls")),
    path("api/config/", include("apps.config.urls")),
    path("api/church/", include("apps.church.urls")),
    path("", home, name="home"),
    # path(r'', include('feincms.urls')),
]


urlpatterns = APPS_URLS + CONFIG_URLS

admin.site.site_header = "Adminitração IBM"
admin.site.site_title = "IBM"
admin.site.index_title = "Igreja Batista Missionária"
