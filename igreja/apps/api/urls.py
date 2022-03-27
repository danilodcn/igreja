from django.urls import include, path

from .routers import account_router

urlpatterns = [
    path("account/", include(account_router.urls)),
]
