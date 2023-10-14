from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Attendance
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date, timedelta


class AttendanceTestCase(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_employee(
            email="test@test.com",
            password="password",
            name="namaaeemplye",
            group="HR"
        )

        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def create_attendance(self, employee, date, attendance_status):
        return Attendance.objects.create(employee=employee, date=date, attendance_status=attendance_status)

    def test_add_attendance(self):
        url = reverse('add_attendance')
        data = {
            'employee': self.user.id,
            'date': '2023-10-13',
            'attendance_status': 'present'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Attendance.objects.count(), 1)
        self.assertEqual(Attendance.objects.get().attendance_status, 'present')

    def test_add_attendance_future_date(self):
        url = reverse('add_attendance')
        future_date = (date.today() + timedelta(days=1)).isoformat()
        data = {
            'employee': self.user.id,
            'date': future_date,
            'attendance_status': 'present'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_add_attendance_duplicate_record(self):
        url = reverse('add_attendance')
        date = '2023-10-13'
        self.create_attendance(employee=self.user, date=date, attendance_status='present')
        data = {
            'employee': self.user.id,
            'date': date,
            'attendance_status': 'absent'
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_attendance(self):
        date = '2023-10-13'
        self.create_attendance(employee=self.user, date=date, attendance_status='present')
        url = reverse('list_attendance', args=[date])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
