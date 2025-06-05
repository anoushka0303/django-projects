from django.contrib import admin
from .models import Course, Syllabus

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('course', 'week', 'topic')