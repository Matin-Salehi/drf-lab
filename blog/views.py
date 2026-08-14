from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

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
