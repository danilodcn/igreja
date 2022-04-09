from rest_framework import filters, generics, views, viewsets
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
    queryset = Post.objects.filter(status=Post.PUBLISHED)

    def get(self, request, slug):
        return Response({"Danilo": slug})
