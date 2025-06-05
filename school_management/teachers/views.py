from django.shortcuts import render
from .models import Teacher, Timetable

def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})

def timetable_list(request):
    timetables = Timetable.objects.all()
    return render(request, 'teachers/timetable_list.html', {'timetables': timetables})