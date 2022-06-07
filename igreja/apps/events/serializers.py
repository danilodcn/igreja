from rest_framework import serializers

from igreja.apps.account.serializers import AddressSerializer
from igreja.apps.church.serializers import ChurchDetailSerializer

from .models import Category, Event


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        exclude = ["created_at", "updated_at"]


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    church = ChurchDetailSerializer()

    class Meta:
        model = Event
        exclude = ["created_at", "updated_at"]
