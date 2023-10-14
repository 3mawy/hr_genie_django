from django.contrib.auth.base_user import BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser


class EmployeeManager(BaseUserManager):
    def create_employee(self, email, password, name, group, is_staff=False, is_superuser=False):
        email = self.normalize_email(email)
        employee = self.model(email=email, name=name, group=group, is_staff=is_staff, is_superuser=is_superuser)
        employee.set_password(password)
        employee.save()
        return employee

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_employee(email, password, **extra_fields)


class Employee(AbstractUser):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=20, choices=[('HR', 'HR'), ('Normal Employee', 'Normal Employee')])

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'group']
    first_name = None
    last_name = None
    username = None
    objects = EmployeeManager()
