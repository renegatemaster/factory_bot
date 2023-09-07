from uuid import uuid4

from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet

from users import models as m
from users import serializers as s


class UserRegisterViewSet(
    GenericViewSet,
    CreateModelMixin,
):
    serializer_class = s.UserRegisterSerializer
    queryset = m.User.objects.all()


class UserTokenViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = s.UserTokenSerializer

    @action(methods=["PUT"], detail=False)
    def get_bot_token(self, request):
        user = m.User.objects.get(id=request.user.id)

        if not user.token:
            while True:
                try:
                    generated_token = uuid4()
                    m.User.objects.get(token=generated_token)
                except m.User.DoesNotExist:
                    break

            user.token = generated_token
            user.save()

        serializer = s.UserTokenSerializer(user)
        return Response(serializer.data)
