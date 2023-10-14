from django.urls import path
from attendance.views import add_attendance, list_attendance

urlpatterns = [
    path('attendance/add', add_attendance, name='add_attendance'),
    path('attendance/<str:date>', list_attendance, name='list_attendance'),

]
