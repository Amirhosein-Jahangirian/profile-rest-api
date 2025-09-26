# rest framework imports
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication


# local imports
from .models import UserProfile
from . import serializers
from . import permissions


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle CRUD in profiles """
    serializer_class = serializers.ProfileSerializer
    queryset = UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.IsOwnerOrReadOnly,)
