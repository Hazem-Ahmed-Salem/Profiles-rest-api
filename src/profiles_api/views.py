from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from profiles_api import models
from profiles_api import serializers
from rest_framework.authentication import TokenAuthentication
from profiles_api import permissions


class APIViewFeatures(APIView):
    """Test APIView"""
    serializer_class = serializers.APIFeaturesSerializer

    def get(self,request,format=None):
        """Return a list of APIView features"""

        an_APIView = [
            'Uses HTTP methods as function (get,patch,post,put,delete)',
            'Is similar to a traditional Djagno view',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]

        return Response({'message':'Hello',
                        'an APIView':an_APIView})
    
    def post(self,request):
        """Create a hello message with our name"""
        
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name  = serializer.validated_data.get('name')
            message = f"hello {name}"
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
                )
        
    def put(self ,request ,pk=None):
        """handle updating an object"""

        return Response({"Method":"PUT"})

    def patch(self ,request ,pk=None):
            """handle partial update of an object"""

            return Response({"Method":"patch"})

    def delete(self ,request ,pk=None):
        """handle deleting an object"""

        return Response({"Method":"delete"})


class ViewSetFeatures(viewsets.ViewSet):
    """Test API ViewSet"""
    
    serializer_class = serializers.APIFeaturesSerializer

    def list(self,request):
        a_viewset =[
            'Uses actions (list, create, retrieve, update, partial update, destroy)',
            'Automatically maps to URLs using Routers',
            'Provide more functionality with less code',
        ]
        return Response({
            "message":"Hello",
            "a_viewset":a_viewset,
        })
    
    def create(self,request):
        """Create a hello message """
        serializer = self.serializer_class( data= request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'hello {name} nice to meet you!'
            return Response({"message":message})
        else:
            return Response(
                serializer.errors,
                status= status.HTTP_400_BAD_REQUEST
            )
        
    def retrieve(self,request,pk=None):
        """Handle getting an object by id"""

        return Response({"http_method":"GET"})
    
    def update(self,request,pk=None):
        """Handle updating an object"""
        
        return Response({'http_method':"PUT"})
    
    def partial_update(self,request,pk=None):
        """handle updating part of an object"""
        
        return Response({"http_method":"PATCH"})
    
    def destroy(self,request,pk=None):
        """Handle removing an object"""

        return Response({"http_method":"delete"})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    """Handel creating and updating profiles"""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes =(TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)

