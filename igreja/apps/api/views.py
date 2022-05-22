from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from igreja.apps.account.models import CustomUser
from igreja.apps.account.serializers import UserSerializer
from igreja.apps.api.serializers.blog import PostSerializer
from igreja.apps.api.serializers.user import ListUserSerializer, NewUserSerializer


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


class GetLoggedUser(generics.views.APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request: Request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
