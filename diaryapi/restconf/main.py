import constant
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        # 'rest_framework.authentication.BasicAuthentication',
        # "rest_framework_jwt.authentication.JSONWebTokenAuthentication",
        # "rest_framework.authentication.SessionAuthentication",
        # django-oauth-toolkit >= 1.0.0
        'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
        'rest_framework_social_oauth2.authentication.SocialAuthentication',
    ],
    "DEFAULT_PERMISSION_CLASSES": [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PAGINATION_CLASS": "diaryapi.restconf.pagination.DiaryAPIPagination",
    "DEFAULT_FILTER_BACKENDS": (
        "rest_framework.filters.SearchFilter",
        "rest_framework.filters.OrderingFilter",
    ),
    "SEARCH_PARAM": "q",
    "ORDERING_PARAM": "ordering",
}

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = constant.SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = constant.SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET


SOCIAL_AUTH_FACEBOOK_KEY = constant.SOCIAL_AUTH_FACEBOOK_KEY
SOCIAL_AUTH_FACEBOOK_SECRET = constant.SOCIAL_AUTH_FACEBOOK_SECRET


# Define SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE to get extra permissions from Google.
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
    'https://www.googleapis.com/auth/userinfo.email',
    'https://www.googleapis.com/auth/userinfo.profile',
]
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id, name, email'
}

OAUTH2_PROVIDER = {
        'ACCESS_TOKEN_EXPIRE_SECONDS': 60 * 60 * 48,
        'OAUTH_SINGLE_ACCESS_TOKEN': True,
        'OAUTH_DELETE_EXPIRED': True
 }

SECRET_KEY = constant.SECRET_KEY

AUTHENTICATION_BACKENDS = (
    # Facebook OAuth2
    'social_core.backends.facebook.FacebookAppOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    # Google OAuth2
    'social_core.backends.google.GoogleOAuth2',

    # DRF Social OAuth
    'rest_framework_social_oauth2.backends.DjangoOAuth2',

    # Django
    'django.contrib.auth.backends.ModelBackend',
)
