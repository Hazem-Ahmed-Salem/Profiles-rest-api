from rest_framework import serializers

class APIFeaturesSerializer(serializers.Serializer):
    """Serializes a name field for testing the APIView"""

    name = serializers.CharField(max_length=10)
