from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import GenericViewSet

from telegram_messages import models as m
from telegram_messages import serializers as s


class MessagesViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
):
    permission_classes = (IsAuthenticated,)
    serializer_class = s.MessageSerializer

    def get_queryset(self):
        return m.Message.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
