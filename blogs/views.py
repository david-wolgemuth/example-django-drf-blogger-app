from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Author, Blog, Favorite
from .serializers import (
    AuthorSerializer,
    BlogSerializer,
    FavoriteSerializer,
)
from .detail_serializers import (
    AuthorDetailSerializer,
    BlogDetailSerializer,
    FavoriteDetailSerializer,
)


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Authors to be viewed or edited.
    """
    queryset = Author.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.detail:
            return AuthorDetailSerializer
        else:
            return AuthorSerializer


class BlogViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Blogs to be viewed or edited.
    """
    queryset = Blog.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.detail:
            return BlogDetailSerializer
        else:
            return BlogSerializer


class FavoriteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Favorites to be viewed or edited.
    """
    queryset = Favorite.objects.all()
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.detail:
            return FavoriteDetailSerializer
        else:
            return FavoriteSerializer



# ------------------------------
#
#
#
#
#
#
#
#

class BlogExplicitViewSet(viewsets.ViewSet):
    @action(methods=["GET", "POST"], detail=False)
    def list_or_create(self, request):
        if request.method == "GET":
            queryset = Blog.objects.all()
            data = BlogSerializer(queryset, many=True).data
            return Response(data, status=200)

        else:
            serializer = BlogSerializer(request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=400)

            blog = serializer.save()
            return Response(serializer.data, status=201)
