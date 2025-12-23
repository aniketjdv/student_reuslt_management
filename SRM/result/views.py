from django.shortcuts import render

# Create your views here.
def student(request):
    # return HttpResponse("Hello world.")
    return render(request,'result/student.html')