from rest_framework.views import APIView
from rest_framework import generics, mixins, permissions, authentication
from rest_framework.response import Response

from .serializers import DiarySerializer, DiaryDetailSerializer
from diary.models import Diary
from accounts.api.permissions import IsOwnerOrNotAllowed, IsSelfUserOrAdminUserOrNotAllowed


class DiaryAPIDetailView(
    mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.RetrieveAPIView
):
    permission_classes = [permissions.IsAuthenticated,
                          IsOwnerOrNotAllowed, ]
    queryset = Diary.objects.all()
    serializer_class = DiaryDetailSerializer
    lookup_field = "id"

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DiaryAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DiarySerializer
    search_fields = ("user__username", "title", "text")
    ordering_fields = ("user__username", "timestamp", "title")
    queryset = Diary.objects.all()

    def get(self, request, *args, **kwargs):
        if not request.user.is_superuser:
            return Response({"detail": "Method Not Allowed"}, status=405)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
