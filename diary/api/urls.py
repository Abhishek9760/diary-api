from django.urls import path, include
from .views import DiaryAPIView, DiaryAPIDetailView

app_name = "diary"

urlpatterns = [
    path("", DiaryAPIView.as_view()),
    path("<int:id>/", DiaryAPIDetailView.as_view(), name="detail"),
]
