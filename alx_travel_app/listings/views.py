from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ListingSerializer


class HelloView(APIView):
    def get(self, request):
        return Response({"message": "Hello from ALX Travel API!"})
