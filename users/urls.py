

from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('teacher_signup/', views.teacher_signup, name = 'teacher_signup'),
    path('login/', views.login, name = 'login'),
    path('instructor_actions/', views.instructor_actions, name = 'instructor_actions'),
    path('student_actions/', views.student_actions, name = 'student_actions'),
]