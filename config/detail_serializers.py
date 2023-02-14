from django.contrib.auth.models import User, Group, Permission


from blogs.serializers import AuthorSerializer

from .serializers import UserSerializer, GroupSerializer, PermissionSerializer


class UserDetailSerializer(UserSerializer):
    author_set = AuthorSerializer(many=True, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)

    class Meta(UserSerializer.Meta):
        model = User
        fields = UserSerializer.Meta.fields + [
            'author_set'
        ]


class GroupDetailSerializer(GroupSerializer):
    user_set = UserSerializer(many=True, read_only=True)
    permissions = PermissionSerializer(many=True, read_only=True)

    class Meta(GroupSerializer.Meta):
        fields = GroupSerializer.Meta.fields + ['user_set']

