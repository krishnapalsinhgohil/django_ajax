from django.shortcuts import render

from .models import College, Student
from .student_form import StudentForm


# Create your views here.
def index(req):
    clglst = College.objects.all()
    return render(req, "index.html", {'form': StudentForm, 'clglst': clglst})


def show_details(req):
    id = req.POST.get("val")
    lst = Student.objects.filter(college_name=id)
    return render(req, 'details.html', {'lst': lst})
