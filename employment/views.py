from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView


class employment(APIView):
    def get(self, request):
        return Response({"message": "get method"})
    
    def post(self, request):
        return Response({"message": "post method"})
    
    def put(self, request):
        return Response({"message": "put method"})
    
    def delete(self, request):
        return Response({"message": "delete method"})