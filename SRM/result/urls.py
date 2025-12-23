
from django.urls import path
from . import views
from .views import *
urlpatterns = [

    path('', views.student,name='student'),
    path("student-dashboard/", student_dashboard, name="student_dashboard"),
     path("admin-panel/", admin_dashboard, name="admin_dashboard"),
    path("add-student/", add_student, name="add_student"),
    path("add-teacher/", add_teacher, name="add_teacher"),
    path("add-subject/", add_subject, name="add_subject"),
    path("add-marks/", add_marks, name="add_marks"),
]
