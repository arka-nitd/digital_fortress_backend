from rest_framework import viewsets
from users.serializers import UserSerializer, CreateUserSerializer
from users.models import User
from rest_framework.permissions import IsAdminUser


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

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