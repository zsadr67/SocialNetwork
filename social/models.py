from django.db import models
#from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

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


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('post', 'user')

    def __str__(self):
        return f'{self.user.username} likes {self.post}'


class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE ,related_name='follower')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f'{self.user.username} follows {self.following}'



