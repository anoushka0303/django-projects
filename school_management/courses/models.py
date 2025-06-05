from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=20, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.name

class Syllabus(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    topic = models.CharField(max_length=100)
    week = models.IntegerField()

    def __str__(self):
        return f"{self.course.name} - Week {self.week}"