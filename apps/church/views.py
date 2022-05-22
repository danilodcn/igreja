from rest_framework import viewsets

from . import models, serializers


class ChurchViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Church.objects.filter(active=True).order_by("is_default")
    serializer_class = serializers.ChurchSerializer
