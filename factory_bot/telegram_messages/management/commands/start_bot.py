from django.conf import settings
from django.core.management.base import BaseCommand
from telegram import Update
from telegram.ext import CommandHandler, Filters, MessageHandler, Updater

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        TOKEN_WAS_FOUND_MESSAGE = "Ваш токен: {token}\nОжидаем входящее сообщение..."
        TOKEN_WAS_NOT_FOUND_MESSAGE = "Токен не найден.\nВведите ваш токен."
        TOKEN_WAS_ADDED_MESSAGE = "Токен {token} принят.\nОжидаем входящее сообщение..."
        INCORRECT_TOKEN_MESSAGE = "Токен недоступен.\nПопробуйте другой токен."

        def start(update, context) -> None:
            user_id = update.effective_user.id

            try:
                user = User.objects.get(telegram_chat_id=user_id)
                update.message.reply_text(
                    TOKEN_WAS_FOUND_MESSAGE.format(token=user.token)
                )

            except User.DoesNotExist:
                update.message.reply_text(TOKEN_WAS_NOT_FOUND_MESSAGE)

        def main_handler(update, context) -> None:
            user_id = update.effective_user.id

            try:
                user = User.objects.get(telegram_chat_id=user_id)
                update.message.reply_text(
                    TOKEN_WAS_FOUND_MESSAGE.format(token=user.token)
                )

            except User.DoesNotExist:
                token = update.message.text.strip()

                try:
                    user = User.objects.get(token=token)
                except User.DoesNotExist:
                    update.message.reply_text(INCORRECT_TOKEN_MESSAGE)

                if user.telegram_chat_id:
                    update.message.reply_text(INCORRECT_TOKEN_MESSAGE)

                else:
                    user.telegram_chat_id = user_id
                    user.save()
                    update.message.reply_text(
                        TOKEN_WAS_ADDED_MESSAGE.format(token=token)
                    )

        updater = Updater(token=settings.TELEGRAM_BOT_TOKEN)
        updater.dispatcher.add_handler(CommandHandler("start", start))
        updater.dispatcher.add_handler(
            MessageHandler(Filters.text & ~Filters.command, main_handler)
        )
        updater.start_polling(allowed_updates=Update.ALL_TYPES)
