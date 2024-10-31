from django.shortcuts import render
from enroll.models import Student
from enroll.forms import StudentRegistration
# Create your views here.

def studentinfo(request):
    stud=Student.objects.all()
    return render(request,'enroll/studetails.html',{'stu':stud})

def showformdata(request):
    fm=StudentRegistration(auto_id=True,label_suffix='B ',initial={'name':'Binod','email':'shresthabinod334@gmail.com'})
    fm.order_fields(field_order=['first_name','name','email'])
    return render(request,'enroll/userregistration.html',{'form':fm})