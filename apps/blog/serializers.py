from rest_framework import serializers

from apps.account.models import CustomUser

from .models import Category, Post


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["created_at", "updated_at"]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "email", "get_full_name"]


class PostSerializerBase(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    # author = AuthorSerializer(view_name="customuser-detail")
    author = AuthorSerializer()

    class Meta:
        model = Post
        exclude = []


class PostListSerializer(serializers.HyperlinkedModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Post
        fields = [
            "author",
            "title",
            "subtitle",
            "publish_date",
            "resume",
            "url",
            "image",
        ]


class PostDetailSerializer(serializers.HyperlinkedModelSerializer):
    categories = CategorySerializer(many=True)
    # author = AuthorSerializer(view_name="customuser-detail")
    author = AuthorSerializer()

    class Meta:
        model = Post
        exclude = []
