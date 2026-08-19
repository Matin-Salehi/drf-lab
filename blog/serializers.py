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

def check_title(data):
    if data['title'] == "game":
        raise serializers.ValidationError({"title":"Game is invalid from function validators"})

class CheckTitle:
    def __call__(self, data):
        if data['title'] == "game":
            raise serializers.ValidationError({"title": "Game is invalid from class based validators"})

class ArticleSerializer(serializers.ModelSerializer):
    # status = serializers.BooleanField(write_only=True)
    class Meta:
        model = Article
        fields = ('id', 'title','status', 'content')
        validators = [
            CheckTitle(),
        ]
        # read_only_fields = ['status']

    # def validate_title(self, value):
    #     if value == "game":
    #         raise serializers.ValidationError("game just for robot no one can use this")
    #     return value

    # def validate(self, attrs):
    #     if attrs['title'] == "game" and attrs['status'] == True:
    #         raise serializers.ValidationError({"status" :"you cant create game content with status True"})
    #     return attrs

