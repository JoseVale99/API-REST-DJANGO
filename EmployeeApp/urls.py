from django.conf.urls import url
from EmployeeApp import views


urlpatterns = [
   url(r'^department$',views.DepartmentApi),
   url(r'^department/([0-9]+)$', views.DepartmentApi),

   url(r'^employee$',views.EmployeeApi),
   url(r'^employee/([0-9]+)$', views.EmployeeApi),
]
