from rest_framework import serializers

from igreja.apps.account.serializers import AdressSerializer

from . import models


class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Church
        exclude = ["created_at", "updated_at", "code"]


class ChurchDetailSerializer(ChurchSerializer):
    address = AdressSerializer()


class ChurchMinisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ChurchMinistry
        exclude = ["created_at", "updated_at"]


class MinisterSerializer(serializers.ModelSerializer):
    ministry = ChurchMinisterSerializer()

    class Meta:
        model = models.Ministry
        exclude = ["created_at", "updated_at"]
