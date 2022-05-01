from rest_framework import serializers

from apps.account.models import CustomUser

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["created_at", "updated_at"]


class AuthorSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_full_name")
    image = serializers.ImageField(source="get_image")

    class Meta:
        model = CustomUser
        fields = ["email", "name", "image"]


class PostSerializerBase(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    # author = AuthorSerializer(view_name="customuser-detail")
    author = AuthorSerializer()

    class Meta:
        model = Post
        exclude = []


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()
    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        fields = [
            "id",
            "author",
            "title",
            "subtitle",
            "publish_date",
            "resume",
            "url",
            "slug",
            "image",
            "categories",
        ]


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    # author = AuthorSerializer(view_name="customuser-detail")
    author = AuthorSerializer()

    class Meta:
        model = Post
        exclude = []
