from users import viewsets as v


def register(router):
    router.register("register", v.UserRegisterViewSet, basename="register")
    router.register("token", v.UserTokenViewSet, basename="token")
