import datetime

from django.contrib.auth import get_user_model
from django.utils import timezone

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse


User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "uri"]

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse(
            "api-user:detail", kwargs={"username": obj.username}, request=request
        )


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True)
    message = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "password2",
            "message",
        ]
        extra_kwargs = {"password": {"write_only": True}}

    def get_message(self, obj):
        return "Thank you for registering."

    def validate_username(self, value):
        qs = User.objects.filter(username__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this username already exists.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("Email is required")
        qs = User.objects.filter(email__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(
                "User with this email already exists.")
        return value

    def validate(self, data):
        pw = data.get("password")
        pw2 = data.get("password2")
        if pw != pw2:
            raise serializers.ValidationError("Passwords must match.")
        return data

    def create(self, validated_data):
        user_obj = User(
            username=validated_data.get("username"), email=validated_data.get("email")
        )
        user_obj.set_password(validated_data.get("password"))
        user_obj.save()
        return user_obj
