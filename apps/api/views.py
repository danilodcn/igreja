from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response

from apps.account.models import CustomUser
from apps.api.serializers.blog import PostSerializer
from apps.api.serializers.user import ListUserSerializer, NewUserSerializer
from apps.blog.models import Post
from apps.core import pagination


class CreateUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = NewUserSerializer
    allowed_methods = ["POST", "OPTIONS"]


class ListUserViewSet(viewsets.ViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = ListUserSerializer

    def list(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(
            queryset, many=True, context={"request": request}
        )
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = self.queryset.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = self.serializer_class(user, context={"request": request})
        return Response(serializer.data)
