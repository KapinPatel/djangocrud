from django.shortcuts import render
from rest_framework import viewsets
from crudApp.models import Company,Employee
from crudApp.serializers import CompanySerializer, EmpSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.
class CrudViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class= CompanySerializer
    
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):
        try:   
            company=Company.objects.get(pk=pk)
            emps=Employee.objects.filter(company=company)
            emps_serializers= EmpSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializers.data)
        except Exception as ex:
            return Response({
                'message':'Error'+str(ex),
            })


class EmpViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class= EmpSerializer