"""learn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from school.views import add_notice, add_teacher, get_notice,home,about, add_student, contact, login_student, login_teacher, logout, login_principal, notice, remove_student, remove_teacher, sclass

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home.as_view(), name='index'),
    path('about',about,name="about"),
    path('contact', contact,name="contact"),
    path('class',sclass, name="class"),
    #login_principal
    path('login_principal',login_principal.as_view(),name='login_principal'),
    path('add_teacher',add_teacher.as_view(),name='add_teacher'),
    #teacher_login
    path('login_teacher',login_teacher,name="login_teacher"),
    #student_login
    path('add_student',add_student,name='add_student'),
    path('login_student', login_student, name="login_student"),
    #logout
    path('logout',logout,name='logout'),
    # remove_student
    path('remove_student', remove_student, name='remove_student'),
    # remove_teacher
    path('remove_teacher', remove_teacher, name='remove_teacher'),
    # notice
    path('notice',notice, name="notice"),
    path('add_notice',add_notice,name='add_notice'),
    path('get_notice',get_notice,name="get_name"),
    
]
