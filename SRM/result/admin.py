from django.contrib import admin
from .models import Studentdemo
# Register your models here.

from .models import (
    Class,
    Subject,
    ClassSubject,
    Student,
    Teacher,
    Exam,
    Marks,
    Result,
    Attendance
)

admin.site.register(Studentdemo)
# -----------------------------
# Class Admin
# -----------------------------
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'section', 'year')
    list_filter = ('year',)
    search_fields = ('class_name', 'section')


# -----------------------------
# Subject Admin
# -----------------------------
@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name', 'subject_code', 'max_marks', 'min_marks')
    search_fields = ('subject_name', 'subject_code')


# -----------------------------
# ClassSubject Admin
# -----------------------------
@admin.register(ClassSubject)
class ClassSubjectAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'subject')
    list_filter = ('class_name',)
    search_fields = ('class_name__class_name', 'subject__subject_name')


# -----------------------------
# Student Admin
# -----------------------------
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'roll_number',
        'first_name',
        'last_name',
        'class_name',
        'gender'
    )
    list_filter = ('class_name', 'gender')
    search_fields = ('roll_number', 'first_name', 'last_name')


# -----------------------------
# Teacher Admin
# -----------------------------
@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email')


# -----------------------------
# Exam Admin
# -----------------------------
@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('exam_name', 'year', 'term')
    list_filter = ('year', 'term')
    search_fields = ('exam_name',)


# -----------------------------
# Marks Admin
# -----------------------------
@admin.register(Marks)
class MarksAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'exam',
        'subject',
        'marks_obtained',
        'grade'
    )
    list_filter = ('exam', 'subject')
    search_fields = (
        'student__roll_number',
        'student__first_name',
        'subject__subject_name'
    )


# -----------------------------
# Result Admin
# -----------------------------
@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = (
        'student',
        'exam',
        'total_marks',
        'percentage',
        'grade',
        'result_status'
    )
    list_filter = ('exam', 'result_status')
    search_fields = (
        'student__roll_number',
        'student__first_name'
    )


# -----------------------------
# Attendance Admin
# -----------------------------
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('student', 'class_name', 'date', 'status')
    list_filter = ('status', 'class_name')
    search_fields = (
        'student__roll_number',
        'student__first_name'
    )