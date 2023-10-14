from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from api_auth.decorators import is_hr
from employees.models import Employee
from employees.serializers import EmployeeSerializer
from django.core.exceptions import ObjectDoesNotExist


@api_view(['POST'])
@permission_classes([IsAuthenticated])
@is_hr
def add_employee(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        employee = serializer.save()
        return Response({'id': employee.id, 'message': 'Employee Added successfully'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
@is_hr
def edit_employee(request, employee_id):
    try:
        employee = Employee.objects.get(id=employee_id)
    except ObjectDoesNotExist:
        return Response({'message': 'Employee not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = EmployeeSerializer(employee, data=request.data, partial=True)

    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Employee details updated successfully'}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all().order_by('id')
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
