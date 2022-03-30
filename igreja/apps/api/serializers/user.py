from apps.account.models import Address, CustomUser, Profile
from rest_framework import serializers


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        exclude = ["updated_at", "created_at"]


class ProfileListSerializer(serializers.ModelSerializer):
    gender = serializers.SerializerMethodField()

    class Meta:
        model = Profile
        exclude = ["updated_at", "created_at", "user", "address"]

    def get_gender(self, obj: Profile):
        return obj.get_gender_display()


class ListUserSerializer(serializers.HyperlinkedModelSerializer):
    full_name = serializers.SerializerMethodField()
    address = AddressSerializer(source="profile.address")
    profile = ProfileListSerializer()

    class Meta:
        model = CustomUser
        exclude = ["password", "groups", "user_permissions"]

    def get_full_name(self, obj: CustomUser):
        return obj.get_full_name()


class NewUserSerializer(serializers.ModelSerializer):
    profile = ProfileListSerializer()

    class Meta:
        model = CustomUser
        fields = (
            "id",
            "email",
            "password",
            "first_name",
            "last_name",
            "profile",
        )
        extra_kwargs = {
            "email": {"required": True},
            "password": {"required": False, "write_only": True},
            "first_name": {"required": True},
            "last_name": {"required": True},
        }

    def create(self, validated_data):
        del validated_data["profile"]
        if self.is_valid():
            user: CustomUser = CustomUser.objects.create(**validated_data)
            ProfileListSerializer().update(user.profile, validated_data)
        else:
            serializers.ValidationError("não é valido")

        return user
