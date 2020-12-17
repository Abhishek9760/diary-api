from django.contrib import admin
from django.urls import path, include

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/diary/", include("diary.api.urls", namespace="api-diary")),
    path("api/user/", include("accounts.api.user.urls", namespace="api-user")),
    path("api/auth/", include("accounts.api.urls", namespace="api-auth")),
]
