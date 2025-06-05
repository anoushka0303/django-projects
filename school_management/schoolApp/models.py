from django.db import models

class Student(models.Model):
    roll_no = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100, default = "None")
    dob = models.DateField()
    gender = models.CharField(max_length=10, default = "Female")
    address = models.TextField()
    guardian_name = models.CharField(max_length=100, default = "None")
    guardian_contact = models.CharField(max_length=15, default = "None")

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(max_length=10, choices=[('Present', 'Present'), ('Absent', 'Absent')])

    def __str__(self):
        return f"{self.student.name} - {self.date}"