from rest_framework import routers

from .views import CreateUserViewSet, ListUserViewSet

account_router = routers.DefaultRouter()

account_router.register("user/create", CreateUserViewSet, basename="create")
account_router.register("user/list", ListUserViewSet)
