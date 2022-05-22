from django.urls import include, path

from . import views
from .routers import router

urlpatterns = [
    path("", include(router.urls)),
]
