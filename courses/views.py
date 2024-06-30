from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from . forms import CourseForm
from .models import Course

# Create your views here.


def home(request):
    #return HttpResponse('Allah Is Almighty')
    return render(request, 'html/base.html', context = {})


def create_course(request):
    #return HttpResponse('Course Created')
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit = False)
            course.instructor = request.user
            course.save()
    else:
        form = CourseForm()
    return render(request, 'html/create_course.html', {'form': form})



def course_enrollment(request, id):
    course = get_object_or_404(Course, id = id)
    if request.user not in course.students.all():
        course.students.add(request.user)
    else:
        return HttpResponse('Already Enrolled')
    return redirect('student_actions')


def view_courses(request):
    all_course = Course.objects.all()
    return render(request, 'html/view_courses.html', {'courses': all_course})

def enrolled_courses(request):
  student = request.user
  courses = student.student_courses.all()
  return render(request, 'html/enrolled_courses.html', {'courses': courses})


def show_course(request, id):
    course = get_object_or_404(Course, id = id)
    return render(request, 'html/show_course.html', {'course': course})


def instructor_view_courses(request):
    all_course = Course.objects.filter(instructor=request.user)  #Course.objects.all()
    return render(request, 'html/instructor_view_courses.html', {'courses': all_course})



def update_course(request, id):
    course = get_object_or_404(Course, id = id)
    instructor_id = course.instructor.id 
    if request.user.id != instructor_id:
        return HttpResponse('You are not allowed to update, You can just update your own created courese')
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('instructor_actions')
    else:
        form = CourseForm(instance=course)
    
    return render(request, 'html/update_course.html', {'form': form, 'course': course})


def delete_course(request, id):
    course = get_object_or_404(Course, id = id)
    instructor_id = course.instructor.id 
    if request.user.id != instructor_id:
        return HttpResponse('You are not allowed to Delete, You can just delete your own created courese')
    course.delete()
    return redirect('instructor_actions')



