from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class Message(models.Model):
    """Telegram sent message"""

    text = models.TextField(_("Message text"))
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="messages", verbose_name=_("User")
    )
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("-date_created",)
        verbose_name = _("Message")
        verbose_name_plural = _("Messages")

    def __str__(self):
        return f"Message ID {self.pk} (User {self.user_id})"
