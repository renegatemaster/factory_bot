from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.core.validators import MinLengthValidator
from django.db import models
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, username: str, name: str, password: str, **kwargs):
        user: User = self.model(username=username, name=name, **kwargs)
        user.set_password(password)

        user.save()
        return user

    def create_superuser(self, username: str, name: str, password: str, **kwargs):
        return self.create_user(
            username=username,
            name=name,
            password=password,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    """Custom User model"""

    username = models.CharField(
        _("Username"),
        max_length=127,
        validators=[MinLengthValidator(2)],
        unique=True,
    )
    name = models.CharField(
        _("Name"), max_length=127, validators=[MinLengthValidator(2)]
    )

    token = models.CharField(_("Token"), max_length=127, blank=True, null=True)
    telegram_chat_id = models.CharField(
        _("Telegram chat ID"), max_length=127, blank=True, null=True
    )

    date_created = models.DateTimeField(_("Date created"), auto_now_add=True)

    is_active = models.BooleanField(_("Active"), default=True)
    is_staff = models.BooleanField(_("Is staff"), default=False)
    is_superuser = models.BooleanField(_("Is superuser"), default=False)

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["name"]

    objects = UserManager()

    class Meta:
        verbose_name = _("User")
        verbose_name_plural = _("Users")
        ordering = ["-id"]

    def __str__(self):
        return f"{self.name} ({self.username})"
