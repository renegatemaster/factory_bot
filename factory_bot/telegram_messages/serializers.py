import telegram
from django.conf import settings
from rest_framework.serializers import ModelSerializer, ValidationError

from telegram_messages import models as m
from users.models import User

bot = telegram.Bot(token=settings.TELEGRAM_BOT_TOKEN)


class MessageSerializer(ModelSerializer):
    class Meta:
        model = m.Message
        fields = (
            "text",
            "date_created",
        )

    def create(self, validated_data):
        text: str = validated_data["text"]
        user: User = validated_data["user"]

        if user.telegram_chat_id:
            bot.send_message(
                chat_id=user.telegram_chat_id,
                text=f"{user.name}, я получил от тебя сообщение:\n{text}",
            )

        else:
            raise ValidationError(
                {"non_fields_error": "User does not have connected telegram chat"}
            )

        return super().create(validated_data)
