# rest framework imports
from django.template.context_processors import request
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

# local imports
from . import models
from . import serializers
from . import permissions


class ProfileViewSet(viewsets.ModelViewSet):
    """Handle CRUD of profiles"""
    serializer_class = serializers.ProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.ProfileOwnerUpdateOnly,
        IsAuthenticated,
    )
    filter_backends = (filters.SearchFilter,)
    search_fields = ('email', 'first_name')


class UserLoginApiView(ObtainAuthToken):
    """perform user login with token authentication"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


class ProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle CRUD of feeds"""
    serializer_class = serializers.ProfileFeedItemSerializer
    queryset = models.ProfileFeedItem.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (
        permissions.FeedOwnerUpdateOnly,
        IsAuthenticatedOrReadOnly,
    )

    def perform_create(self, serializer):
        """set newly created feed owner to logged-in user"""
        serializer.save(owner=self.request.user)
