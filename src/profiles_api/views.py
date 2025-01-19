from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets , filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from profiles_api import models
from profiles_api import serializers
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from profiles_api import permissions



    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields =('name','email',)

class UserLoginApiView(ObtainAuthToken):
    """Handle creating user authentication tokens"""

    """renderer_classes makes this view renders as the apiview and the viewsets (viewsets and apiviews have this option by default)"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """Handle  creating ,reading ,and updating profile feed items"""
    authentication_classes = (TokenAuthentication,)
    serializer_class       = serializers.ProfileFeedItemSerializer
    permission_classes     = (
        permissions.UpdateOwnstatus,
        IsAuthenticatedOrReadOnly,
    )
    queryset = models.ProfileFeedItem.objects.all()

    def perform_create(self, serializer):
        """sets the user profile to the logged in user"""
        serializer.save(user_profile=self.request.user)