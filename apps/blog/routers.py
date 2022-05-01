from rest_framework import routers

from . import views

router = routers.DefaultRouter()

router.register("blog", views.BlogViewSet)
router.register("category", views.CategoryListViewSet)
