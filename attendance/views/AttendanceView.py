from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.exceptions import BadRequest

from attendance.models import Attendance
from attendance.serializers import AttendanceSerializer
from api_auth.decorators import is_hr


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@is_hr
def add_attendance(request):
    serializer = AttendanceSerializer(data=request.data)

    if serializer.is_valid():
        employee_id = serializer.validated_data['employee']
        date = serializer.validated_data['date']
        if date > date.today():
            return Response({'message': 'Attendance date cannot be in the future.'}, status=status.HTTP_400_BAD_REQUEST)
        existing_record = Attendance.objects.filter(employee=employee_id, date=date).first()
        if existing_record:
            return Response({'message': 'Attendance record already exists for this date and employee.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer.save()
            return Response({'message': 'Attendance added successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@is_hr
def list_attendance(request, date):
    try:

        attendance_records = Attendance.objects.filter(date=date)

        serializer = AttendanceSerializer(attendance_records, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    except BadRequest as e:
        return Response({'message': 'Error retrieving attendance records'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)