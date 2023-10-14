from django.urls import path
from rest_framework import routers
from employees.views import add_employee, edit_employee, list_employees

router = routers.DefaultRouter()

urlpatterns = [
    path('employees', list_employees, name='list_employees'),
    path('employees/add', add_employee, name='add_employee'),
    path('employees/<str:employee_id>', edit_employee, name='edit_employee'),
]
