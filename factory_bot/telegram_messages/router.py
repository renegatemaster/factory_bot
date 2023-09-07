from telegram_messages import viewsets as v


def register(router):
    router.register("messages", v.MessagesViewSet, basename="messages")
