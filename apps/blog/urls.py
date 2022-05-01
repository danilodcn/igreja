from django.urls import include, path

from . import views
from .routers import router

urlpatterns = [
    path("", include(router.urls)),
    path("list/<slug:slug>/", views.PostViewDetail.as_view()),
]
