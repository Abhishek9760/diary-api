from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse

from diary.api.serializers import DiaryInlineUserSerializer

User = get_user_model()


class UserDetailSerializer(serializers.ModelSerializer):
    uri = serializers.SerializerMethodField(read_only=True)
    diary = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "uri",
            "diary",
        ]

    def get_uri(self, obj):
        request = self.context.get("request")
        return api_reverse(
            "api-user:detail", kwargs={"username": obj.username}, request=request
        )

    def get_diary(self, obj):
        request = self.context.get("request")
        limit = 10
        if request:
            limit_query = request.GET.get("limit")
            try:
                limit = int(limit_query)
            except:
                pass
        qs = obj.diary_set.all().order_by("-timestamp")

        data = {
            "uri": self.get_uri(obj) + "diary/",
            "last": DiaryInlineUserSerializer(
                qs.first(), context={"request": request}
            ).data,
            "recent": DiaryInlineUserSerializer(
                qs[:limit], many=True, context={"request": request}
            ).data,
        }
        return data
