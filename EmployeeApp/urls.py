from django.conf.urls import url
from EmployeeApp import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
   url(r'^department$',views.DepartmentApi),
   url(r'^department/([0-9]+)$', views.DepartmentApi),

   url(r'^employee$',views.EmployeeApi),
   url(r'^employee/([0-9]+)$', views.EmployeeApi),
   url(r'^employee/savefile/([0-9]+)$',views.SaveFile),
]+static(settings.MEDIA_URL, department_root = settings.MEDIA_ROOT)
