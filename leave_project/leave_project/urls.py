"""
URL configuration for leave_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from leave_app import views  # Import views from your app

urlpatterns = [
    path('admin/', admin.site.urls),               # Admin panel
    path('', views.sregister, name='sregister'),  # Registration page
    path('login/', views.slogin, name='slogin'),           # Login page
    path('home/', views.home, name='home'),                # Home page (post-login)
    path('logout/', views.user_logout, name='logout'),     # Logout functionality
    path('dashboard/', views.dashboard, name='dashboard'),
    path('status/', views.student_status, name='student_status'),
]




