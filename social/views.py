from rest_framework import viewsets

from social.models import Profile
from social.serializers import ProfileSerializer


class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
