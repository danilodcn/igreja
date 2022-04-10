from django.db.models import Q
from django.http import Http404
from rest_framework import filters, generics, status, views, viewsets
from rest_framework.request import Request
from rest_framework.response import Response

from apps.core import pagination

from .models import Category, Post
from .serializers import (
    CategorySerializer,
    PostDetailSerializer,
    PostListSerializer,
)


class APIMixin:
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 10

    pagination_class = pagination.PagenationBase


class CategoryListViewSet(APIMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer


class BlogViewSet(APIMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.filter(status=Post.PUBLISHED)
    # serializer_class = PostSerializer
    page_size = 6

    pagination_class = pagination.PagenationBase
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "subtitle"]

    def get_serializer_class(self):
        if self.action == "list":
            return PostListSerializer
        if self.action == "retrieve":
            return PostDetailSerializer

        return PostDetailSerializer

    def get_queryset(self):
        qs = super().get_queryset()
        slug = self.request.query_params.get("slug", None)
        if slug:
            qs.filter(slug=slug)

        return qs


class PostViewDetail(views.APIView):
    queryset = Post.objects.filter(Q(status=Post.PUBLISHED) | Q(test=True))

    def get(self, request: Request, slug):
        post = self.get_object(slug=slug)
        serializer = PostDetailSerializer(
            instance=post, context={"request": request}
        )
        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, **kwargs) -> Post:
        try:
            return self.queryset.get(**kwargs)
        except Post.DoesNotExist:
            raise Http404
