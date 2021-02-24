from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/diary/", include("diary.api.urls", namespace="api-diary")),
    path('api/auth/', include('rest_framework_social_oauth2.urls')),
    path("api/user/", include("accounts.api.user.urls", namespace="api-user")),
    path("api/auth/register/", include("accounts.api.urls", namespace="api-auth")),
] + static(settings.STATIC_URL,
           document_root=settings.STATIC_ROOT)+static(settings.MEDIA_URL,
                                                      document_root=settings.MEDIA_ROOT)
