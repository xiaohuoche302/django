from django.shortcuts import render
from django.http import HttpResponse
from .models import Grade,Students
# Create your views here.

def add(request,a,b):
	c = int(a)+int(b)

	return HttpResponse(str(c))


def home(request):
	return render(request,'home.html')

def grade(request):
	grade = Grade.objects.all()
	print(grade)
	content={}
	content['grade'] = grade
	return render(request,'grade.html',content)

def grade_one(request,gid):
	grade_one = Grade.objects.get(id = gid)
	return render(request,'grade_one.html',locals())

def student(request,sid):
	stu = Students.objects.filter(sgrade_id = sid)
	print(stu)
	return render(request, 'student.html', locals())