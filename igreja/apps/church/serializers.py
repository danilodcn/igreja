from rest_framework import serializers

from igreja.apps.account.serializers import AdressSerializer

from . import models


class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Church
        exclude = ["created_at", "updated_at", "code"]


class ChurchDetailSerializer(ChurchSerializer):
    address = AdressSerializer()
