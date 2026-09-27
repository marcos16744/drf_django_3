from django.contrib.auth.models import User
from rest_framework import serializers


class RegistroSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ["username", "password"]
        extra_kwargs = {
            "password": {"write_only": True}
        }

    def create(self, validated_data):
        usuario = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"]
        )

        return usuario


