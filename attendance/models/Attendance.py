from django.contrib.auth import get_user_model
from django.db import models


class Attendance(models.Model):
    employee = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    date = models.DateField()
    attendance_status = models.CharField(max_length=20, choices=[('present', 'Present'), ('absent', 'Absent')])

