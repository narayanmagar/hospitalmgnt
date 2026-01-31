"""
URL configuration for hospitalmgnt project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from django.http import HttpResponse  # ✅ THIS LINE MUST BE HERE
from accounts.views import role_redirect_view

from accounts.views import register_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('redirect/', role_redirect_view, name='role_redirect'),
    path('admin-dashboard/', lambda r: HttpResponse("Admin Dashboard")),
    path('doctor-dashboard/', lambda r: HttpResponse("Doctor Dashboard")),
    path('nurse-dashboard/', lambda r: HttpResponse("Nurse Dashboard")),
    path('reception-dashboard/', lambda r: HttpResponse("Receptionist Dashboard")),
    path('register/', register_view, name='register'),

]
