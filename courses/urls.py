
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('home/', views.home, name = 'home'),
    path('create_course/', views.create_course, name = 'create_course'),
    path('update_course/', views.update_course, name = 'update_course'),
    path('delete_course/', views.delete_course, name = 'delete_course'),
    path('course_enrollment/<str:id>', views.course_enrollment, name = 'course_enrollment'),
    path('view_courses/', views.view_courses, name = 'view_courses'),
    path('enrolled_courses/', views.enrolled_courses, name = 'enrolled_courses'),
    path('show_course/<int:id>', views.show_course, name = 'show_course'),
    path('instructor_view_courses/', views.instructor_view_courses, name = 'instructor_view_courses'),
    path('update_course/<int:id>', views.update_course, name = 'update_course'),
    path('delete_course/<int:id>', views.delete_course, name = 'delete_course'),

]

