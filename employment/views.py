from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView, status
from employment.models import Employment

from .serializers import DetailEmploymentSerializer, EmploymentSerializer

class Employments(APIView):
    def get(self, request):
        employments = EmploymentSerializer(Employment.objects.all(), many=True)
        return Response(employments.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        employment_serializer = EmploymentSerializer(data=request.data, context={'request': request})
        if employment_serializer.is_valid():
            employment_serializer.save()
            return Response(employment_serializer.data, status=status.HTTP_200_OK)
        return Response(employment_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, employment_id):
        employment = Employment.objects.get(id=employment_id)
        employment_Serializer = EmploymentSerializer(employment, data=request.data, partial=True)
        if employment_Serializer.is_valid():
            employment_Serializer.save()
            return Response(employment_Serializer.data, status=status.HTTP_200_OK)
        return Response(employment_Serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, employment_id):
        employment = Employment.objects.get(id=employment_id)
        employment.delete()
        return Response({"message": "delete 완료"})

class DetailEmployment(APIView):
    def get(self, request, employment_id):
        employment = Employment.objects.get(id=employment_id)
        print(employment.company.name)
        print(dir(employment))
        employment_serializer = DetailEmploymentSerializer(employment)
        return Response(employment_serializer.data, status=status.HTTP_200_OK)
    