from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('admin/')),  # This redirects / to /admin/
    path('admin/', admin.site.urls),
    path('students/', include('schoolApp.urls')),
]