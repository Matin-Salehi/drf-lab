from django.contrib.sites import requests
from django.shortcuts import render
from rest_framework import response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
import requests

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

