from django.contrib.auth import get_user_model

from rest_framework import permissions, generics, pagination
from rest_framework.response import Response
from rest_framework.views import APIView

from accounts.api.permissions import IsSelfUserOrAdminUserOrNotAllowed

from .serializers import UserDetailSerializer
from diary.models import Diary
from diary.api.serializers import DiaryInlineUserSerializer

User = get_user_model()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserDetailSerializer
    permission_classes = [IsSelfUserOrAdminUserOrNotAllowed, ]
    queryset = User.objects.filter(active=True)
    lookup_field = "username"

    def get_serializer_context(self):
        return {"request": self.request}


class UserDiaryAPIView(generics.ListAPIView):
    serializer_class = DiaryInlineUserSerializer
    permission_classes = [IsSelfUserOrAdminUserOrNotAllowed, ]
    ordering_fields = ['timestamp']
    search_fields = ['title', 'text', ]

    def get_queryset(self, *args, **kwargs):
        username = self.kwargs.get("username")
        if not username:
            return Diary.objects.none()
        return Diary.objects.filter(user__username=username)


class UserExistsAPIView(APIView):
    permission_classes = []
    authentication_classes = []

    def get(self, request, *args, **kwargs):
        username = kwargs.get('username')
        email = request.GET.get('email')
        errors = {"username": "", "email": ""}
        if email:
            email_obj = User.objects.filter(email__iexact=email)
            if email_obj.exists():
                errors['email'] = "Already exists"
        if username:
            user_obj = User.objects.filter(username__iexact=username)
            if user_obj.exists():
                errors["username"] = "Already taken"
        return Response(errors, status=200)
