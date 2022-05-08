from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import CustomUser


class UserSerializer(serializers.ModelSerializer):
    name = serializers.CharField(source="get_full_name")
    image = serializers.ImageField(source="get_image")

    class Meta:
        model = CustomUser
        exclude = [
            "password",
            "last_login",
            "date_joined",
            "groups",
            "user_permissions",
        ]


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    user = UserSerializer()
