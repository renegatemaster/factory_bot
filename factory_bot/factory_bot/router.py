from rest_framework import routers

from telegram_messages.router import register as register_telegram_messages
from users.router import register as register_users

router = routers.DefaultRouter()

register_users(router)
register_telegram_messages(router)
