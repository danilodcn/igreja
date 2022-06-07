from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from .models import Address, CustomUser


class AddressSerializer(serializers.ModelSerializer):
    address_type = serializers.CharField(source="get_address_type_display")

    class Meta:
        model = Address
        exclude = ["created_at", "updated_at"]


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
