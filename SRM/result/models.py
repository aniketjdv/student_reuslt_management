from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.
class Studentdemo(models.Model):
    STYPE = [('IT','Information Technology'),
             ('CS','Computer Science'),
             ('MBA','Buisness Admstration')
             ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='img/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=3,choices=STYPE)

    def __str__(self):
        return self.name

# -----------------------------
# Class Model
# -----------------------------
class Class(models.Model):
    class_name = models.CharField(max_length=50)
    section = models.CharField(max_length=10, blank=True, null=True)
    year = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.class_name} {self.section} ({self.year})"


# -----------------------------
# Subject Model
# -----------------------------
class Subject(models.Model):
    subject_name = models.CharField(max_length=100)
    subject_code = models.CharField(max_length=20, unique=True)
    max_marks = models.PositiveIntegerField()
    min_marks = models.PositiveIntegerField()

    def __str__(self):
        return self.subject_name


# -----------------------------
# Class - Subject Mapping
# -----------------------------
class ClassSubject(models.Model):
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('class_name', 'subject')

    def __str__(self):
        return f"{self.class_name} - {self.subject}"


# -----------------------------
# Student Model
# -----------------------------
class Student(models.Model):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    roll_number = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    dob = models.DateField()
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('roll_number', 'class_name')

    def __str__(self):
        return f"{self.roll_number} - {self.first_name}"


# -----------------------------
# Teacher Model
# -----------------------------
class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    subject = models.ForeignKey(Subject, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


# -----------------------------
# Exam Model
# -----------------------------
class Exam(models.Model):
    exam_name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    year = models.PositiveIntegerField()
    term = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return f"{self.exam_name} ({self.year})"


# -----------------------------
# Marks Model
# -----------------------------
class Marks(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    marks_obtained = models.FloatField()
    grade = models.CharField(max_length=5, blank=True)
    remarks = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'exam', 'subject')

    def __str__(self):
        return f"{self.student} - {self.subject} - {self.marks_obtained}"


# -----------------------------
# Result Model
# -----------------------------
class Result(models.Model):
    RESULT_STATUS = (
        ('Pass', 'Pass'),
        ('Fail', 'Fail'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    total_marks = models.FloatField()
    percentage = models.FloatField()
    grade = models.CharField(max_length=5)
    result_status = models.CharField(max_length=10, choices=RESULT_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'exam')

    def __str__(self):
        return f"{self.student} - {self.exam} - {self.result_status}"


# -----------------------------
# Attendance Model (Optional)
# -----------------------------
class Attendance(models.Model):
    STATUS_CHOICES = (
        ('Present', 'Present'),
        ('Absent', 'Absent'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    class_name = models.ForeignKey(Class, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    class Meta:
        unique_together = ('student', 'date')

    def __str__(self):
        return f"{self.student} - {self.date} - {self.status}"



class ChatMessage(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name="teacher_chats")
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    sender = models.CharField(max_length=10, choices=[('Teacher','Teacher'),('Student','Student')])
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} - {self.timestamp}"