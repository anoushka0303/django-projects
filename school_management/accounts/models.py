from django.db import models
from django.contrib.auth.models import User
from schoolApp.models import Student
from teachers.models import Teacher
from django.core.exceptions import ValidationError

# Create your models here.

class Profile(models.Model):
    user_roles = (
        ('student', 'Student'),
        ('teacher', 'Teacher'),
        ('principal', 'Principal'),
    )

    user = models.OneToOneField(User, on_delete= models.CASCADE)
    role = models.CharField(max_length= 20, choices= user_roles)

    student = models.OneToOneField(Student, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.OneToOneField(Teacher, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} ({self.role})"
    
    def clean(self):
        if self.role == 'student' and not self.student:
            raise ValidationError("Student profile must be linked for role 'student'.")
        if self.role == 'teacher' and not self.teacher:
            raise ValidationError("Teacher profile must be linked for role 'teacher'.")
        if self.role == 'principal' and (self.teacher or self.student):
            raise ValidationError("Principal should not be linked to student or teacher models.")
        
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance, role='student')
