from config.serializers import UserSerializer

from .serializers import AuthorSerializer, BlogSerializer, FavoriteSerializer


class AuthorDetailSerializer(AuthorSerializer):
    user = UserSerializer(many=False, read_only=True)
    blog_set = BlogSerializer(many=True, read_only=True)

    class Meta(AuthorSerializer.Meta):
        fields = AuthorSerializer.Meta.fields + ['blog_set']


class BlogDetailSerializer(BlogSerializer):
    author = AuthorSerializer(many=False, read_only=True)
    favorite_set = FavoriteSerializer(many=True, read_only=True)

    class Meta(BlogSerializer.Meta):
        fields = BlogSerializer.Meta.fields + ['author', 'favorite_set', 'content']


class FavoriteDetailSerializer(FavoriteSerializer):
    user = UserSerializer(many=False, read_only=True)
    blog = BlogSerializer(many=False, read_only=True)

    class Meta(FavoriteSerializer.Meta):
        pass