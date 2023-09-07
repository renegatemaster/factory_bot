from django.contrib import admin

from telegram_messages import models as m


@admin.register(m.Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "text",
        "date_created",
    )
    search_fields = ("text",)
    list_filter = ("user__username",)
