from rest_framework import viewsets

from . import models, serializers


class ImageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ImageHomeThroughModel.objects.all()
    serializer_class = serializers.ImageHomeSerialiser


class PageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.HomePageConfig.objects.all()
    serializer_class = serializers.PageHomeSerializer
