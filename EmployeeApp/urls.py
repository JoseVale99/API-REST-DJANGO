from django.conf.urls import url, urls
from EmployeeApp import views


urlpatterns = [
   url(r'^department$',views.DepartmentApi),
   url(r'^department/([0-9]+)$')
]
