from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import serializers
from .models import pages


class ImageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pages.ImageThroughModel.objects.all()
    serializer_class = serializers.ImageSerialiser


class PageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = pages.PageConfig.objects.all()
    serializer_class = serializers.PageConfigSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        church_id = self.request.query_params.get("church_id", "")
        type = self.request.query_params.get("type", "")

        if type:
            qs = qs.filter(type=type)

        if not church_id:
            return qs.filter(church__is_default=True)

        return qs.filter(church_id=church_id)
