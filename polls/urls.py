"""basicapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

# from django.views.generic.base import TemplateView

urlpatterns = [
    path('',views.index,name='home'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/',views.attendance_detail,name='attendance_detail'),
    path('student/<int:stud_id>/attendance',views.attendance,name='attendance'),
    path('teacher/<int:att_id>/ChangeAttendance/',views.change_attendance,name='change_attendance'),
    path('teacher/<slug:stud_id>/<slug:course_id>/attendance/',views.t_attendance_detail,name='t_attendance_detail'),
    path('teacher/<slug:teacher_id>/<int:choice>/Classes/',views.t_clas,name='t_clas'),
    path('teacher/<int:ass_c_id>/attendance/',views.t_attendance,name='t_attendance'),
    path('teacher/<int:ass_c_id>/attendance/confirm/',views.confirm,name='confirm'),
    path('teacher/<int:ass_c_id>/Edit_att/',views.edit_att,name='edit_att'),
    path('teacher/<int:assign_id>/Student/Attendance/',views.t_student,name='t_student'),
    # path('teacher/<int:assign_id>/Students/attendance/', views.t_student, name='t_student'),
    path('teacher/<int:assign_id>/ClassDates/',views.t_class_date,name='t_class_date'),
    path('signup/',views.signup,name='signup'),
    
   
]
