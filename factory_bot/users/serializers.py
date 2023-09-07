from rest_framework.serializers import ModelSerializer

from users import models as m


class UserRegisterSerializer(ModelSerializer):
    class Meta:
        model = m.User
        fields = ("id", "username", "name", "password")
        read_only_fields = ("id",)
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return m.User.objects.create_user(**validated_data)


class UserTokenSerializer(ModelSerializer):
    class Meta:
        model = m.User
        fields = ("token",)
