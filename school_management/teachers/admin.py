from django.contrib import admin
from .models import Teacher, Timetable

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'employee_id', 'subject', 'contact')

@admin.register(Timetable)
class TimetableAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'class_name', 'day', 'time_slot')