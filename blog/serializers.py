from rest_framework import serializers
from .models import Article

class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.EmailField()

class ArticleSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=False)
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()
    status = serializers.BooleanField(required=False)

    def create(self, validated_data):
        return Article.objects.create(**validated_data)