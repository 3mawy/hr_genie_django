from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee

class EmployeeTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_employee(
            email="zzaaaaaa",
            password="password",
            name="namaaeemplye",
            group="HR"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_add_employee(self):
        url = reverse('add_employee')
        data = {
            'email': 'testemployee@example.com',
            'password': 'testpassword',
            'name': 'Test Employee',
            'group': 'Normal Employee'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_employee(self):
        employee = Employee.objects.create(
            email='testemployee@example.com',
            password='testpassword',
            name='Test Employee',
            group='Normal Employee'
        )

        url = reverse('edit_employee', args=[employee.id])
        data = {
            'name': 'Updated Name',
        }
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_list_employees(self):
        Employee.objects.create(
            email='employee1@example.com',
            password='password1',
            name='Employee 1',
            group='HR'
        )
        Employee.objects.create(
            email='employee2@example.com',
            password='password2',
            name='Employee 2',
            group='Normal Employee'
        )

        url = reverse('list_employees')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data), 3)
