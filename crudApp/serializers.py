from rest_framework import serializers
from crudApp.models import Company, Employee


class CompanySerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model= Company
        fields= "__all__"

class EmpSerializer(serializers.ModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"