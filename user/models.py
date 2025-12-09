from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone

from user.manager import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    Custom User model.
    """
    email = models.EmailField(unique=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, default='')

    # Django required fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(blank=True, null=True)

    # Trust system fields
    is_verified = models.BooleanField(
        default=False,
        help_text='Designates whether this user has been verified as trustworthy.'
    )
    trust_score = models.IntegerField(
        default=0,
        help_text='User trust score based on accuracy of submissions.'
    )

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'  # Use email for authentication
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []  # Email & Password are required by default.

    class Meta:
        """Meta information for the User model."""
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def get_full_name(self):
        """Return the full name of the user."""
        return self.name

    def get_short_name(self):
        """Return the short name of the user."""
        return self.name or str(self.email).split('@', maxsplit=1)[0]
