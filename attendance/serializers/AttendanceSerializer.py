from rest_framework import serializers
from attendance.models import Attendance


class AttendanceSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%d-%m-%Y", input_formats=["%d-%m-%Y", "%Y-%m-%d"])

    class Meta:
        model = Attendance
        fields = ['employee', 'date', 'attendance_status']

