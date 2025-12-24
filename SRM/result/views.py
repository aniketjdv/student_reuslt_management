from django.shortcuts import render, get_object_or_404,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def student(request):
    # return HttpResponse("Hello world.")
    return render(request,'result/student.html')

def student_dashboard(request):
    student = None
    marks = None
    result = None
    error = None

    if request.method == "POST":
        roll_number = request.POST.get("roll_number")

        try:
            student = Student.objects.get(roll_number=roll_number)
            marks = Marks.objects.filter(student=student)
            result = Result.objects.filter(student=student).last()
        except Student.DoesNotExist:
            error = "Student not found"

    context = {
        "student": student,
        "marks": marks,
        "result": result,
        "error": error,
    }

    return render(request, "result/student_dashboard.html", context)

def admin_dashboard(request):
    context = {
        "student_count": Student.objects.count(),
        "teacher_count": Teacher.objects.count(),
        "subject_count": Subject.objects.count(),
        "marks_count": Marks.objects.count(),
    }
    return render(request, "result/admin/dashboard.html", context)


def add_student(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("admin_dashboard")
    return render(request, "result/admin/add_student.html", {"form": form})


def add_teacher(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("admin_dashboard")
    return render(request, "result/admin/add_teacher.html", {"form": form})


def add_subject(request):
    form = SubjectForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("admin_dashboard")
    return render(request, "result/admin/add_subject.html", {"form": form})


def add_marks(request):
    form = MarksForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("admin_dashboard")
    return render(request, "result/admin/add_marks.html", {"form": form})

def add_class(request):
    form = ClassForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("admin_dashboard")
    return render(request, "result/admin/add_class.html", {"form": form})


@login_required
def teacher_dashboard(request):
    teacher = Teacher.objects.get(user=request.user)
    students = Student.objects.filter(class_name__in=Class.objects.all())

    context = {
        "teacher": teacher,
        "students": students,
        "marks_count": Marks.objects.filter(subject=teacher.subject).count()
    }
    return render(request, "teacher/dashboard.html", context)


@login_required
def teacher_add_marks(request):
    teacher = Teacher.objects.get(user=request.user)

    form = MarksForm(request.POST or None)
    form.fields['subject'].queryset = Subject.objects.filter(id=teacher.subject.id)

    if form.is_valid():
        form.save()
        return redirect("teacher_dashboard")

    return render(request, "teacher/add_marks.html", {"form": form})


@login_required
def teacher_students(request):
    students = Student.objects.all()
    return render(request, "teacher/students.html", {"students": students})

@login_required
def teacher_chat(request, student_id):
    student = Student.objects.get(id=student_id)
    chats = ChatMessage.objects.filter(student=student)

    if request.method == "POST":
        ChatMessage.objects.create(
            teacher=request.user,
            student=student,
            message=request.POST.get("message"),
            sender="Teacher"
        )

    return render(request, "teacher/chat.html", {
        "student": student,
        "chats": chats
    })