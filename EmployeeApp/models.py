from django.db import models
# Create your models here.

class Departments(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=500)

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeesName = models.CharField(max_length=500)
    Department = models.CharField(max_length=500)
    DateofJoining = models.DateField()
    photoFileName =   models.TextField(blank=True)

    

