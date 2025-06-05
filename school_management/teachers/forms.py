from django import forms
from .models import Teacher, Timetable

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'

class TimetableForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = '__all__'