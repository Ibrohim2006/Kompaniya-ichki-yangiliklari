from django.contrib.auth.models import AbstractUser
from django.db import models
from authentication.managers import UserManager


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True


class UserModel(AbstractUser, TimeStampedModel):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email address")
    is_verified = models.BooleanField(default=False, verbose_name="Is verified")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'user'
        verbose_name = 'User'
        verbose_name_plural = 'Users'
