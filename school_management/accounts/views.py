from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .utils import generate_jwt
from .models import Profile
from django.contrib.auth.models import User

def custom_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            try:
                role = user.profile.role
            except:
                return render(request, 'accounts/login.html', {'error' : 'No Profile Found'})
            if role == 'student':
                return redirect('accounts:student_dashboard')
            elif role == 'teacher':
                return redirect('accounts:teacher_dashboard')
            elif role == 'principal':
                return redirect('accounts:principal_dashboard')
        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid credentials'})
    return render(request, 'accounts/login.html')

def student_dashboard(request):
    return render(request, 'accounts/student_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'accounts/teacher_dashboard.html')

def principal_dashboard(request):
    return render(request, 'accounts/principal_dashboard.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        role = request.POST.get('role')  # assuming you let user pick role or set default

        if User.objects.filter(username=username).exists():
            return render(request, 'accounts/signup.html', {'error': 'Username already taken.'})

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role=role or 'student')  # create related profile

        return redirect('accounts:login')  # redirect to login after signup

    return render(request, 'accounts/signup.html')

def logout_view(request):
    logout(request)
    return redirect('accounts:login')