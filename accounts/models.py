from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager
)


class UserManager(BaseUserManager):
    def create_user(self, email, username, password=None, is_staff=False, is_admin=False,
                    is_active=True):  # add required fields
        if not email:
            raise ValueError("Users must have an email address")
        # if not password:
        #     raise ValueError("Users must have a password")
        if not username:
            raise ValueError("Users must have a username")

        email = self.normalize_email(email)
        user_obj = self.model(
            username=username,
            email=email
        )
        user_obj.set_password(password)  # change the password
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        # user_obj.email = email
        user_obj.save(using=self._db)
        return user_obj

    def create_staffuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
        )

    def create_superuser(self, email, username, password=None):
        user = self.create_user(
            email,
            username,
            password=password,
            is_staff=True,
            is_admin=True
        )


AUTH_PROVIDERS = {'google': 'google', 'username': 'username'}


class User(AbstractBaseUser):
    email = models.EmailField(max_length=255)
    username = models.CharField(
        max_length=255, null=True, blank=True, unique=True)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    auth_provider = models.CharField(
        max_length=255, null=False, blank=False, default=AUTH_PROVIDERS.get('username'))

    objects = UserManager()

    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.username

    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_active(self):
        return self.active

    @property
    def is_admin(self):
        return self.admin
