from django.contrib.auth.models import User, Group

from rest_framework import viewsets
from rest_framework import permissions

from .models import Author, Blog
from .serializers import AuthorSerializer, AuthorDetailSerializer, BlogSerializer, BlogDetailSerializer


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
