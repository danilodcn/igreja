from rest_framework import serializers

from igreja.apps.blog.models import Category, Post

from .user import ListUserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = []


class PostSerializer(serializers.ModelSerializer):

    categories = CategorySerializer(many=True)

    class Meta:
        model = Post
        exclude = []
