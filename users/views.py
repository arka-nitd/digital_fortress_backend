from rest_framework import viewsets, status
from rest_framework.generics import GenericAPIView
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from social_django.utils import psa

from users.permissions import NotLoggedIn
from users.serializers import UserSerializer, CreateUserSerializer, AccessTokenSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()

    serializers = {
        'create': CreateUserSerializer,
        'default': UserSerializer,
    }
    
    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def get_permissions(self):
        if self.action in ('create',):
            self.permission_classes = [IsAdminUser, ]
        return super(self.__class__, self).get_permissions()


class LoginView(GenericAPIView):

    permission_classes = (NotLoggedIn, )

    serializers = {
        'auth': AuthTokenSerializer,
        'default': AccessTokenSerializer,
    }

    def get_serializer_class(self):
        backend = self.kwargs.get('backend', None)
        return self.serializers.get(backend, self.serializers['default'])

    def post(self, request, backend):
        if backend == 'auth':  # Admin Login
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                user = serializer.validated_data['user']
                Token.objects.get_or_create(user=user)
                return Response(UserSerializer(user).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:  # Player Social Login
            user = register_by_access_token(request, backend)
            if user and user.is_active:
                Token.objects.get_or_create(user=user)
                return Response(UserSerializer(user).data)
            else:
                return Response("Bad Credentials, check the Access Token and/or the UID", status=403)

@psa()
def register_by_access_token(request, backend):

    token = request.data.get('access_token', None)
    user = request.backend.do_auth(token)
    if user:
        return user
    else:
        return None


class LogoutView(APIView):

    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_205_RESET_CONTENT)