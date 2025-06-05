from django.urls import path
from . import views

urlpatterns = [
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('timetables/', views.timetable_list, name='timetable_list'),
]