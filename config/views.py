from django.contrib.auth.models import User, Group, Permission

from rest_framework import viewsets
from rest_framework import permissions

from .serializers import UserSerializer, UserDetailSerializer, GroupSerializer, GroupDetailSerializer, PermissionSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.detail:
            return UserDetailSerializer
        else:
            return UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.detail:
            return GroupDetailSerializer
        else:
            return GroupSerializer


class PermissionViewSet(viewsets.ModelViewSet):
    queryset = Permission.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        return PermissionSerializer
