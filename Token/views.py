from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializer import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated





class StudentModelViewApi(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    
    
