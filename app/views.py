# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals
#
# from django.shortcuts import render
# from .models import Student,Teacher
#
# # Create your views here.
# def StudentInfo(request):
#     qs = Student.objects.all()
#     qs1=Teacher.objects.all()
#     con={"qs":qs,"qss1":qs1}
#
#     return render(request,"student.html",con)
#
# def TeacherInfo(request):
#
#     return render(request,"teacher.html")
#
#
# def Student_Details(request):
#     t_name=request.POST.get("t1")
#     name=request.POST.get("t2")
#     contact=request.POST.get("t3")
#     r=Teacher(name=t_name)
#     r.save()
#     Student(teacher=r,name=name,contact=contact).save()
#     qs = Student.objects.all()
#
#     return  render(request,"student.html",{"qs":qs})


from django.shortcuts import render
from .models import Skill,Subskill


# Create your views here.
def home(request):
    skill = Skill.objects.all()
    subskill =Subskill.objects.all()
    context = {'skills':skill,
               'subskills':subskill}
    return render(request, 'skill.html', context)