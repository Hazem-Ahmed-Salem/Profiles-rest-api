from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from profiles_api import serializers


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
