
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from django.shortcuts import get_object_or_404, get_list_or_404

from social.models import Profile, Post
from social.serializers import ProfileSerializer, PostSerializer



class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class ProfileView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]

    queryset = Profile.objects.select_related("user").all()
    serializer_class = ProfileSerializer

    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]



class PostView(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def perform_create(self, serializer):
    #     # موقع ساخت پست، نویسنده همون یوزر لاگین شده باشه
    #     serializer.save(user=self.request.user)

