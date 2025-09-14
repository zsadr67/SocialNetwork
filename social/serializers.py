from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from social.models import Profile, Post, Like


class ProfileSerializer(ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    email = serializers.CharField(source='user.email', read_only=True)


    class Meta:
        model = Profile
        fields = ['id', 'username', 'email' , 'bio' ,'avatar', 'location' ]


class PostSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    likes_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'user', 'content', 'likes_count' , 'is_liked','created_at']


    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_is_liked(self, obj):
        request = self.context.get('request')
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False



class LikeSerializer(ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ['id' ,'user', 'post' , 'created_at']
        read_only_fields = ['user']