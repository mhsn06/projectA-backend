from rest_framework import serializers 
class JabinSerializer(serializers.Serializer):
  greetings = serializers.CharField()
class JabinSerializer2(serializers.Serializer):
  greetings = serializers.CharField()