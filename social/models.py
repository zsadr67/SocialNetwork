from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE , related_name='profile')
    avatar = models.ImageField(upload_to='avatars', null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    location = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.user.username



class Post(models.Model):
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text


