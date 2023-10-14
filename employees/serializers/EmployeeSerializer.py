from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from employees.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        max_length=100,
        validators=[UniqueValidator(queryset=Employee.objects.all())],
        required=True
    )
    password = serializers.CharField(write_only=True, required=True, min_length=8)

    class Meta:
        model = Employee
        fields = ['id', 'email', 'password', 'name', 'group']

    def create(self, validated_data):
        employee = Employee.objects.create_employee(
            email=validated_data['email'],
            password=validated_data['password'],
            name=validated_data['name'],
            group=validated_data['group']
        )
        return employee
