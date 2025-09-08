from  django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer


class CreateUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id','username' ,'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)