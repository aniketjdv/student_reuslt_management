
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
    path("add-class/", add_class, name="add_class"),
    path("teacher/", teacher_dashboard, name="teacher_dashboard"),
    path("teacher/add-marks/", teacher_add_marks, name="teacher_add_marks"),
    path("teacher/students/", teacher_students, name="teacher_students"),
    path("teacher/chat/<int:student_id>/", teacher_chat, name="teacher_chat"),

]
