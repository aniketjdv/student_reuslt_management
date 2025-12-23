from django import forms
from .models import Student, Teacher, Subject, Marks, Exam

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name', 'email', 'phone', 'subject']


class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


class ExamForm(forms.ModelForm):
    class Meta:
        model = Exam
        fields = '__all__'


class MarksForm(forms.ModelForm):
    class Meta:
        model = Marks
        fields = ['student', 'class_name', 'exam', 'subject', 'marks_obtained', 'grade']
