from apps.users.models import User
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.viewsets import GenericViewSet
from apps.users.UserSerializers import UserSerializer, LoginSerializer
from django.contrib.auth import login
from django.contrib.auth.models import update_last_login
from knox.views import LoginView as KnoxLoginView
from knox.models import AuthToken
from rest_framework.response import Response


class ListUserApiView(ListModelMixin, GenericViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    queryset = User.objects.all()

class LoginView(KnoxLoginView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)

        AuthToken.objects.filter(user=user).delete()

        token = AuthToken.objects.create(user=user)[1]
        update_last_login(None, user)

        return Response({
            'user': {
                'id': user.id,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            },
            'token': token,
        })