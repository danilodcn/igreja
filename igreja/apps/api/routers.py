from rest_framework import routers

from .views import CreateUserViewSet, ListUserViewSet

router = routers.DefaultRouter()

router.register("user/create", CreateUserViewSet, basename="create")
router.register("user/list", ListUserViewSet)
