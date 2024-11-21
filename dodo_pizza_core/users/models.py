from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models

from users.managers import CustomUserManager


class CustomUser(AbstractUser):

    username = None
    phone_number = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(6)],
        unique=True,
    )

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = CustomUserManager

    class Meta:
        verbose_name_plural = 'Кастомные пользователи'
        verbose_name = 'Кастомный пользователь'
