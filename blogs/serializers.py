from rest_framework import serializers

from config.serializers import UserSerializer

from .models import Author, Blog



class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['url', 'id', 'user', 'name']


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = [
            'url',
            'id',
            'author',
            'title',
            # 'content',
        ]


class AuthorDetailSerializer(AuthorSerializer):
    user = UserSerializer(many=False, read_only=True)
    blog_set = BlogSerializer(many=True, read_only=True)

    class Meta(AuthorSerializer.Meta):
        fields = AuthorSerializer.Meta.fields + ['blog_set']


class BlogDetailSerializer(BlogSerializer):
    author = AuthorSerializer(many=False, read_only=True)

    class Meta(BlogSerializer.Meta):
        fields = BlogSerializer.Meta.fields + ['author', 'content']
