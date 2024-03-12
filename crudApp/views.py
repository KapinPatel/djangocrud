from django.shortcuts import render
from rest_framework import viewsets
from crudApp.models import Company,Employee
from crudApp.serializers import CompanySerializer, EmpSerializer
# Create your views here.
class CrudViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer

class EmpViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmpSerializer