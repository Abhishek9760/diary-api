from django.urls import path

from .views import AuthAPIView, RegisterAPIView

app_name = "auth"

urlpatterns = [
    # path("", AuthAPIView.as_view()),
    path("", RegisterAPIView.as_view()),
]
