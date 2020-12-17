from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from diary.models import Diary
from accounts.api.serializers import UserPublicSerializer


class DiarySerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    uri = serializers.SerializerMethodField(read_only=True)
    # text = serializers.SerializerMethodField()
    # text = serializers.ModelField(model_field=Diary._meta.get_field('text'))

    # def to_representation(self, obj):
    #     data = super(DiarySerializer, self).to_representation(obj)
    #     if(len(data['text']) > 10):
    #         data['text'] = data['text'][:20] + "..."
    #     return data

    class Meta:
        model = Diary
        fields = (
            "id",
            "user",
            "title",
            "text",
            "image",
            "timestamp",
            "updated",
            "uri",
        )
        read_only_fields = ["user"]

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse("api-diary:detail", kwargs={"id": obj.id}, request=request)

    def validate(self, data):
        text = data.get("text")
        image = data.get("image")
        if not (image or text):
            raise serializers.ValidationError("Text or Image is Required")
        return data


class DiaryInlineUserSerializer(DiarySerializer):

    class Meta:
        model = Diary
        fields = [
            "id",
            "text",
            "title",
            "image",
            "timestamp",
            "uri",
        ]
        read_only_fields = ["user"]


class DiaryDetailSerializer(DiarySerializer):

    # def to_representation(self, obj):
    #     data = super(DiaryDetailSerializer, self).to_representation(obj)
    #     return data

    class Meta:
        model = Diary
        fields = [
            "id",
            "text",
            "title",
            "image",
            "uri",
            "user",
            "timestamp",
            "updated"
        ]
        read_only_fields = ["user"]
