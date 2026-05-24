from django.contrib.auth import get_user_model
from rest_framework.generics import CreateAPIView
from todos_auth.serializers import RegisterSerializer


User = get_user_model()


class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

