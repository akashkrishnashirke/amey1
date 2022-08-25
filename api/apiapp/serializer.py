from rest_framework import serializers
from .models import Employee

class EmployeeSer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"

class EmployeeSerName(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ['ename']