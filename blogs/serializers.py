from rest_framework import serializers

from .models import Author, Blog, Favorite


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [
            # 'url',
            # 'oops',
            'id', 'user', 'name']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            # 'url',
            'id',
            'author',
            'title',
            # 'content',
        ]

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = [
            'url',
            'id',
            'user',
            'blog',
        ]



# -----------------
# Verbose / "Explicit" Serializer
#
#
#
#
#
#


class BlogExplicitSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    author = serializers.IntegerField()
    title = serializers.CharField()
    content = serializers.CharField()

    class Meta:
        model = Blog
        fields = [
            # 'url',
            'id',
            'author',
            'title',
            'content',
        ]


