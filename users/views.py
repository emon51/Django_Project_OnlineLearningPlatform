from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User, Group
from django.contrib import auth, messages

# Create your views here.

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return HttpResponse("You are already registered.")
        
        data = User.objects.create_user(username = username, email = email, password = password)
        #user = data.save()
        user = data
        data.save
        group = Group.objects.get(name = 'Student')
        user.groups.add(group)
        #return HttpResponse('Register Successfull')
        return redirect('student_actions') #url_name: 'student_actions'
    else:
        return render(request, 'html/signup.html')
    

def teacher_signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(email=email).exists() or User.objects.filter(username=username).exists():
            return HttpResponse("You are already registered.")

        data = User.objects.create_user(username = username, email = email, password = password)
        #user = data.save()
        user = data
        data.save
        group = Group.objects.get(name = 'Instructor')
        user.groups.add(group)
        #return HttpResponse('Register Successfull')
        return redirect('instructor_actions')
    else:
        return render(request, 'html/signup.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user:
            auth.login(request, user)
            #return HttpResponse('Login Successfull')
            #return redirect('create_course')
            if user.groups.filter(name='Instructor').exists():
                return redirect('instructor_actions')
            else:
                return redirect('student_actions')

        else:
            #return HttpResponse('Invalid Informations. Try Again')
            messages.info(request, 'Invalid Informations. Try Again')
            return redirect('login')
    else:
        return render(request, 'html/login.html')
    


def instructor_actions(request):
    return render(request, 'html/instructor_actions.html')

def student_actions(request):
    return render(request, 'html/student_actions.html')


