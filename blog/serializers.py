from rest_framework import serializers
from .models import Article
from django.contrib.auth.models import User

# class UserSerializer(serializers.Serializer):
#     username = serializers.CharField(max_length=50)
#     last_name = serializers.CharField(max_length=50)
#     email = serializers.EmailField()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'last_name', 'email')

# class ArticleSerializer(serializers.Serializer):
#     id = serializers.IntegerField(required=False)
#     title = serializers.CharField(max_length=100)
#     content = serializers.CharField()
#     status = serializers.BooleanField(required=False)
#
#     def create(self, validated_data):
#         return Article.objects.create(**validated_data)

class ArticleSerializer(serializers.ModelSerializer):
    status = serializers.BooleanField(write_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title','status', 'content')
        read_only_fields = ['status']
