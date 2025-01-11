from rest_framework.views import APIView
from rest_framework.response import Response



class APIViewFeatures(APIView):
    """Test APIView"""

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