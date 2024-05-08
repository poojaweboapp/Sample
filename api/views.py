from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class ItemListView(APIView):
    def get(self, request):
        items = ['item1', 'item2', 'item3']  # Dummy list of items
        return Response(items, status=status.HTTP_200_OK)