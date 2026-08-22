from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework import response, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests
from django.contrib.auth.models import User
from .models import Article
from .serializers import UserSerializer, ArticleSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import BlockListPermission, IsUserOrReadOnly


@api_view(['GET', 'POST'])
def index(request):
    if request.method == 'POST':
        name = request.data.get('name')
        lastname = request.data.get('lastname')
        return Response({'message': f'HELLO {name} {lastname}'})
    if request.method == 'GET':
        name = request.GET.get("name")
        return Response({'name': name})
    return Response({'message': 'Hello World'})


class IndexView(APIView):
    def get(self, request):
        name = request.GET.get('name')
        return Response({'message': f'Hello {name}'})
    def post(self, request):
        data = request.data
        return Response({'message': f'Hello {data['name']} {data['lastname']}'})



class GetCryptoPrice(APIView):
    def get(self, request):
        url = "https://api.abantether.com/api/v1/manager/otc/ticker"
        response = requests.get(url)
        data = response.json()
        markets = data["data"]["markets"]
        symbol = request.GET.get("symbol")

        for market in markets.values():
            if symbol.upper() == market["symbol"]:
                return Response({
                    "symbol": market["symbol"],
                    "buy price": market["buy_price"],
                    "sell price": market["sell_price"],
                })


class SerializerView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        ser = UserSerializer(instance=queryset, many=True)
        return Response(data=ser.data)



class ArticleListView(APIView):
    def get(self, request):
        queryset = Article.objects.filter(status=True)
        serializer = ArticleSerializer(queryset, many=True)
        return Response(data=serializer.data)

class ArticleDetailView(APIView):
    def get(self, request, pk):
        instance = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance)
        return Response(data=serializer.data)


class AddArticleView(APIView):
    permission_classes = [
        BlockListPermission,
        IsAuthenticated
    ]
    def post(self, request):
        serializer = ArticleSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "Added Successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateArticleView(APIView):
    permission_classes = [
        IsAuthenticated,
        IsUserOrReadOnly
    ]
    def put(self, request, pk):
        instance = Article.objects.get(id=pk)
        self.check_object_permissions(request, instance)
        serializer = ArticleSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.update(instance=instance, validated_data=serializer.validated_data)
            return Response({"response": "Updated Successfully"},)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ChackToken(APIView):
    # authentication_classes = [TokenAuthentication]
    def get(self, request):
        user = request.user
        return Response({"name": user.username})