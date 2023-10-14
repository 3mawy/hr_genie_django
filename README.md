# HR Genie Django

HR Genie is an API for a web application that allows an HR to easily manage and navigate Employees and their attendance.

## Features
- HR employee can login to system.
- HR employee can add, edit, and list employee records.
- HR employee can add and list attendance records for employees in specific dates.
- Requires user authentication and HR group for access.
- Uses serializers for data validation and serialization in the API.
- Prevent the creation of duplicate attendance records for the same employee on the same date.

## Installation and Setup
```
docker-compose up 
```
## Testing
```
python manage.py test attendance employees
```
# API REFERENCE
# 📁 Collection: Auth 


## End-point: login
### Method: POST
>```
>http://localhost:8004/api/login
>```
### Body (**raw**)

```json
{
    "email": "test@test.com",
    "password":"password"
}
```

### Response: 200
```json
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NzMxOTQ5OCwiaWF0IjoxNjk3MjMzMDk4LCJqdGkiOiIwNzE2YmM2N2Y4ZTQ0YTU3ODI4NzZmZmQyYThmMjQzOSIsInVzZXJfaWQiOjMyfQ.HMdjtuOvcBgnImgUKLf6yAfr-eQLckDZDAQofI06AyI",
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3NTMzMDk4LCJpYXQiOjE2OTcyMzMwOTgsImp0aSI6IjE3NjU0MWE2YTI5ZDRjYThiYWJkZjhkZjVmYWUyOWQ0IiwidXNlcl9pZCI6MzJ9.uIUK-DUI6HxVBuyNxA6xHyLrakET20xg_fWdzk8jgNE"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: refresh token
### Method: POST
>```
>http://localhost:8004/api/token/refresh
>```
### Body (**raw**)

```json
{"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzM2NzkzOCwiaWF0IjoxNjkzMjgxNTM4LCJqdGkiOiJjY2QyMzA1ZGMyZjA0ZTZhYmQ5ODQ4NjJjZWQ4ZTY5OCIsInVzZXJfaWQiOjMyfQ.hMhRlvwc6f6UrTD4i899CF3Qfdh3qJt5RueQ2zrKKck"}
```


### Response: 200
```json
{
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjkzNTgxNTczLCJpYXQiOjE2OTMyODE1MzgsImp0aSI6IjE0MjM4NjIzMjcyZTQ3Nzc4MDE0NmVjZjA1MGQ0MzliIiwidXNlcl9pZCI6MzJ9.rDJI7SkhddpUsjdbRrujOHTXJoBeI7vX-mzMirfvWJI",
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5MzM2Nzk3MywiaWF0IjoxNjkzMjgxNTczLCJqdGkiOiI4ZmI4OWUxM2VkNWE0ZDZkYmViMTcwOTc2ODhiNzVmYSIsInVzZXJfaWQiOjMyfQ.IscvNcjy53nGskEE0rdt0I0Z_Af12rGoNDk-WpsI7qo"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: employees 


## End-point: add new employee
### Method: POST
>```
>http://localhost:8004/api/employees/add
>```
### Body (**raw**)

```json
{
    "email": "test@test.com",
    "password": "password",
    "name": "name test",
    "group": "HR"
}
```

### Response: 201
```json
{
    "id": 32,
    "message": "Employee Added successfully"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: edit employee
### Method: PATCH
>```
>http://localhost:8004/api/employees/1
>```
### Body (**raw**)

```json
{
    "name": "change test",
    "group": "HR"
}
```

### Response: 200
```json
{
    "message": "Employee details updated successfully"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: get all employees
### Method: GET
>```
>http://localhost:8004/api/employees
>```
### Response: 200
```json
[
  {
    "id": 1,
    "email": "test@hr.com",
    "name": "test hr",
    "group": "HR"
  },
  {
    "id": 2,
    "email": "test@hr2.com",
    "name": "jack doe",
    "group": "Normal Employee"
  },
  {
    "id": 3,
    "email": "test@hr3.com",
    "name": "jack doe",
    "group": "Normal Employee"
  }
]
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃
# 📁 Collection: attendance 


## End-point: add employee attendance
### Method: POST
>```
>http://localhost:8004/api/attendance/add
>```
### Body (**raw**)

```json
{
    "employee": "1" ,
    "date": "2023-10-13" ,
    "attendance_status": "present"
}
```

### Response: 201
```json
{
    "message": "Attendance added successfully"
}
```


⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃ ⁃

## End-point: list attendance
### Method: GET
>```
>http://localhost:8004/api/attendance/2023-10-13
>```
### Response: 200
```json
[
    {
        "employee": 1,
        "date": "13-10-2023",
        "attendance_status": "absent"
    },
    {
        "employee": 2,
        "date": "13-10-2023",
        "attendance_status": "absent"
    },
    {
        "employee": 2,
        "date": "13-10-2023",
        "attendance_status": "present"
    }
]
```


