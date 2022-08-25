from django.shortcuts import render
from .models import Employee
from .serializer import EmployeeSer,EmployeeSerName
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

# Create your views here.

class EmployeeTable(APIView):
    def get(self,request):
        empobj= Employee.objects.all()
        serobj=EmployeeSer(empobj,many=True)
        return Response(serobj.data)
    def post(self,request):
        serobj= EmployeeSer(data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_201_CREATED)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
    def put(self,request,pk):
        empobj = Employee.objects.get(pk=pk)
        serobj = EmployeeSer(empobj,data=request.data)
        if serobj.is_valid():
            serobj.save()
            return Response(serobj.data,status=status.HTTP_200_OK)
        return Response(serobj.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,pk):
        empobj = Employee.objects.get(pk=pk)
        empobj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EmployeeName(APIView):
    def get(self,request):
        empobj= Employee.objects.all()
        serobj= EmployeeSerName(empobj,many=True)
        return Response(serobj.data)



