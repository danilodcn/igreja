from rest_framework import serializers

from apps.church.models import MemberType
from apps.church.serilaizers import ChurchSerializer

from . import models


class MemberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        exclude = ["created_at", "updated_at", "code"]


class ImageHomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageHome
        exclude = []


class ChurchBodySerializer(serializers.ModelSerializer):
    member_type = MemberTypeSerializer()

    class Meta:
        model = models.ChurchBodySection
        exclude = []


class ImageHomeSerialiser(serializers.ModelSerializer):
    imagehome = ImageHomeSerializer()

    class Meta:
        model = models.ImageHomeThroughModel
        exclude = ["homepageconfig", "id"]


class PageHomeSerializer(serializers.ModelSerializer):
    images = ImageHomeSerialiser(many=True)
    body = ChurchBodySerializer(many=True, source="church_body_sections")
    church = ChurchSerializer()

    class Meta:
        model = models.HomePageConfig
        exclude = []
