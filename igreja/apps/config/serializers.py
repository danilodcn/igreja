from rest_framework import serializers

from igreja.apps.church.models import MemberType
from igreja.apps.church.serializers import ChurchDetailSerializer

from . import models


class MemberTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberType
        exclude = ["created_at", "updated_at", "code"]


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ImageHome
        exclude = ["id", "name", "order"]


class ChurchBodySerializer(serializers.ModelSerializer):
    member_type = MemberTypeSerializer()

    class Meta:
        model = models.ChurchBodySection
        exclude = ["created_at", "updated_at"]


class ImageSerialiser(serializers.ModelSerializer):
    image = ImageSerializer()

    class Meta:
        model = models.ImageThroughModel
        exclude = ["id", "page", "order"]


class PageContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.PageContent
        exclude = ["page", "id", "created_at", "updated_at"]


class BasePageSerializer(serializers.ModelSerializer):
    images = ImageSerialiser(many=True)
    sections = PageContentSerializer(many=True, source="content")
    church = ChurchDetailSerializer()
    type_display = serializers.CharField(source="get_type_display")

    class Meta:
        model = models.PageConfig
        exclude = ["created_at", "updated_at"]


class PageIndexSerializer(BasePageSerializer):
    body = ChurchBodySerializer(many=True, source="page_content_ministry")
