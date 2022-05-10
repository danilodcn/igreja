from rest_framework import serializers

from apps.account.serializers import AdressSerializer

from . import models


class ChurchSerializer(serializers.ModelSerializer):
    address = AdressSerializer()

    class Meta:
        model = models.Church
        exclude = ["created_at", "updated_at", "code"]
