from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from social.models import Profile, Post


class ProfileSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)


    class Meta:
        model = Profile
        fields = ['id', 'username', 'email' , 'bio' ,'avatar', 'location' ]


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'