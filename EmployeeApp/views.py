from re import T
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from EmployeeApp.models import Employee,Departments
from EmployeeApp.serializers import EmployeeSerializer, DepartmentSerializer

# Create your views here.


@csrf_exempt
def DepartmentApi(request, id=0):
    if request.method == 'GET':
        departments  = Departments.objects.all()
        department_serealizer = DepartmentSerializer(departments,
        many=True)
        return JsonResponse(department_serealizer.data, safe=False)
    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serealizer = DepartmentSerializer(data=department_data)
        if department_serealizer.is_valid():
            department_serealizer.save()
            return JsonResponse('Add successfully!', safe=False)
        return JsonResponse('Add failed!', safe=False)    
    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Departments.objects.get(DepartmentID=department_data['DepartmentID'])
        department_serealizer = DepartmentSerializer(department, data=department_data)
        if department_serealizer.is_valid():
            department_serealizer.save()
            return JsonResponse('Update successfully!', safe=False)
        return JsonResponse('Update failed!', safe=False)
    elif request.method == 'DELETE':
        department = Departments.objects.get(DepartmentID=id)
        department.delete() 
        return JsonResponse('Delete successfully!',safe=False)
        
    

