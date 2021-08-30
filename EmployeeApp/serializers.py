from rest_framework import fields, serializers
from EmployeeApp.models import Departments, Employees


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields = ('DepartmentID','DepartmentName')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = (
            'EmployeeID',
            'EmployeesName',
            'Department',
            'DateofJoining',
            'photoFileName'
            )