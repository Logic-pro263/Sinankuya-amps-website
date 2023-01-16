from django.db import models
from django.contrib.auth.models import User


class Comments(models.Model):
    full_name = models.CharField(max_length=120)
    comments = models.CharField(max_length=1000)

    def __str__(self):
        return self.full_name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, verbose_name="auteur", on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="blog/", verbose_name="image de blog", name="image_blog"
    )
    post = models.ForeignKey(
        Comments,
        related_name="comment",
        verbose_name="Article",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f"Titre: {self.title} - Auteur: {self.author}"


class Message(models.Model):
    full_name = models.CharField(max_length=120)
    email = models.EmailField()
    message = models.TextField(max_length=1500)

    def __str__(self):
        return f"Nom complet: {self.full_name} - Email: {self.email}"
