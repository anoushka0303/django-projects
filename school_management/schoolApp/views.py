from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from .models import Student
from .forms import StudentForm

class StudentListView(ListView):
    model = Student
    context_object_name = 'students'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Student {form.instance.first_name} {form.instance.last_name} created successfully!")
        return response

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy('student_list')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"Student {form.instance.first_name} {form.instance.last_name} updated successfully!")
        return response

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy('student_list')

    def delete(self, request, *args, **kwargs):
        student = self.get_object()
        response = super().delete(request, *args, **kwargs)
        messages.success(self.request, f"Student {student.first_name} {student.last_name} deleted successfully!")
        return response