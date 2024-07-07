"""
URL configuration for Dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.signin, name='Login'),
    path('register', views.register, name='register'),
    path('signrecord', views.signrecord, name='signrecord'),
    path('dashboard', views.dash, name='dashboard'),
    path('loginpage', views.loginpage, name='loginpage'),
    path('doclogin/', views.doclogin, name='doclogin'),
    path('docsignin', views.docsignin, name='docsignin'),
    path('docregister', views.docregister, name='docregister'),
    path('docsignrecord', views.docsignrecord, name='docsignrecord'),
    path('docdash', views.docdash, name='docdash'),
]
