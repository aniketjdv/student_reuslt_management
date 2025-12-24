from django.shortcuts import render, get_object_or_404,redirect
from .models import Student, Teacher, Subject, Marks
from .forms import StudentForm, TeacherForm, SubjectForm, MarksForm


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