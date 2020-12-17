from django.urls import path

from .views import UserDetailAPIView, UserDiaryAPIView, UserExistsAPIView


app_name = "users"

urlpatterns = [
    path("<str:username>/", UserDetailAPIView.as_view(), name="detail"),
    path("<str:username>/diary/", UserDiaryAPIView.as_view(), name="diary-list"),
    path("<str:username>/exists/", UserExistsAPIView.as_view(), name="diary-exists"),
]
