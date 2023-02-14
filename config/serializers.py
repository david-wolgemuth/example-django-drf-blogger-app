from django.contrib.auth.models import User, Group, Permission
from rest_framework import serializers


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'id', 'name', 'permissions']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'url',
            'id',
            # 'last_login',
            'is_superuser',
            'username',
            # 'first_name',
            # 'last_name',
            'email',
            'is_staff',
            'is_active',
            # 'date_joined',
            'groups',
            'user_permissions',
        ]


class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['url', "id", "name", "codename", "content_type"]
