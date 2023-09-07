from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from django.utils.translation import gettext_lazy as _

from users import models as m

admin.site.unregister(Group)


@admin.register(m.User)
class UserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("username", "name", "password")}),
        (_("Bot info"), {"fields": ("token", "telegram_chat_id")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_created")}),
    )

    list_display = (
        "id",
        "username",
        "name",
        "token",
        "telegram_chat_id",
        "date_created",
        "last_login",
    )
    list_filter = ("is_superuser", "is_active")
    search_fields = (
        "name",
        "username",
        "token",
        "telegram_chat_id",
    )

    readonly_fields = (
        "last_login",
        "date_created",
    )
