from django.shortcuts import render
from rest_framework import viewsets
from crudApp.models import Company
from crudApp.serializers import CompanySerializer
# Create your views here.
class CrudViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer