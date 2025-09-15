
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import permissions

from django.shortcuts import get_object_or_404, get_list_or_404

from social.models import Profile, Post, Like, Follow
from social.serializers import ProfileSerializer, PostSerializer, FollowSerializer

from django.contrib.auth import get_user_model

User = get_user_model()


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        #print ("obj.user is:" , obj.user , "request.user is: " ,request.user)
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

    def perform_create(self, serializer):
        # موقع ساخت پست، نویسنده همون یوزر لاگین شده باشه
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'] , permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):

        post = self.get_object()

        like , created = Like.objects.get_or_create(post=post, user=request.user)

        if not created:
            like.delete()
            return Response({"status" : "unlike"} ,status=status.HTTP_200_OK)
        return Response({"status" : "like"} ,status=status.HTTP_201_CREATED)


# class LikeView(APIView):
#     authentication_classes = [JWTAuthentication]
#     permission_classes = [IsAuthenticated]
#
#     def post(self, request, post_id):
#         post = get_object_or_404(Post, pk=post_id)
#
#         like , created = Like.objects.get_or_create(post=post, user=request.user)
#
#         if not created:
#             like.delete()
#             return Response({"status" : "unlike"} ,status=status.HTTP_200_OK)
#         return Response({"status" : "like"} ,status=status.HTTP_201_CREATED)


class FollowView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):

        try:
            user_to_follow = User.objects.get(pk=user_id)

            if user_to_follow.id == request.user.id:
                return Response({"error" : "You cannot follow yourself"} ,status=status.HTTP_400_BAD_REQUEST)

            follow, created = Follow.objects.get_or_create(follower=request.user , following=user_to_follow)

            if not created:
                follow.delete()
                return Response({"status" : "unfollow"} ,status=status.HTTP_200_OK)

            serializer = FollowSerializer(follow)
            return Response(serializer.data ,status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({"error" : "User does not exist"} ,status=status.HTTP_400_BAD_REQUEST)









