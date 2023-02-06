from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.


class Author(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.TextField()


class Blog(models.Model):
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
    )
    title = models.TextField()
    content = models.TextField()
