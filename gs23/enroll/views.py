from django.shortcuts import render
from enroll.models import Student
from enroll.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    stud=Student.objects.all()
    return render(request,'enroll/studetails.html',{'stu':stud})

def showformdata(request):
    fm=StudentRegistration()
    return render(request,'enroll/userregistration.html',{'form':fm})