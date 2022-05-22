from django.urls import include, path

from igreja.apps.api.views import GetLoggedUser

from .routers import router

urlpatterns = [
    path("", include(router.urls)),
    path("login/", GetLoggedUser.as_view()),
]
