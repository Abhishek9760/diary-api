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

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = "984792856479-vbl9011ikj3ais9375j98f9mlik84v68.apps.googleusercontent.com"
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = "WDYZHuD4vNPUjq7mXMhRh0kD"


SOCIAL_AUTH_FACEBOOK_KEY = '3375293559265744'
SOCIAL_AUTH_FACEBOOK_SECRET = '8e5ac9c00edba750845ebe4d2ec096f6'


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
