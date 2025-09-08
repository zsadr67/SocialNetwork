from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from user.serializers import CreateUserSerializer


class CreateUserView(APIView):

    def post(self, request):
        serializer = CreateUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()  # ساخت کاربر اینجا انجام میشه
        return Response(serializer.data, status=status.HTTP_201_CREATED)