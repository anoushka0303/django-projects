from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('accounts:login')),  # Redirect root to login page

    path('accounts/', include(('accounts.urls', 'accounts'), namespace='accounts')),
    path('students/', include(('schoolApp.urls', 'schoolApp'), namespace='schoolApp')),
    path('teachers/', include(('teachers.urls', 'teachers'), namespace='teachers')),
    #path('courses/', include(('courses.urls', 'courses'), namespace='courses')),

    path('admin/', admin.site.urls),
]