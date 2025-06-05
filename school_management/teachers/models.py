from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100)
    employee_id = models.CharField(max_length=20, unique=True)
    subject = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Timetable(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    class_name = models.CharField(max_length=50)
    day = models.CharField(max_length=10)
    time_slot = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.teacher.name} - {self.class_name} - {self.day}"