from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from applications.account.serializers import RegisterSerializer


class RegistrationView(APIView):
    def post(self, request):
        data = request.data
        serializer = RegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response('Successfully signed up', status=status.HTTP_201_CREATED)