from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from . import models, serializers


class ImageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.ImageThroughModel.objects.all()
    serializer_class = serializers.ImageSerialiser


class PageHomeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.PageConfig.objects.all()
    serializer_class = serializers.PageIndexSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        church_id = self.request.query_params.get("church_id", "")
        type = self.request.query_params.get("type", "")
        
        if type:
            qs = qs.filter(type=type)

        # import ipdb; ipdb.set_trace()
        if not church_id:
            return qs.filter(church__is_default=True)

        return qs.filter(church_id=church_id)
