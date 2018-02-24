from django.test.client import Client
from django.urls import reverse
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import ProfileSerializer


class Profile(APIView):
    """API resource for user profile.

    get:
    Get user profile.

    put:
    Update user profile.
    """

    def get(self, request: Request) -> Response:
        user = request.user
        serializer = ProfileSerializer(user.profile)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request: Request) -> Response:
        user = request.user
        serializer = ProfileSerializer(user.profile, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
