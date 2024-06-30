# Online Learning Platform 

### Motivation
Build a user-friendly platform that enables instructors to create and manage courses, and students to enroll, access content efficiently.

## Features

- **Instructor Features:**
  - Create, update, and delete courses.
  - Add, update, and delete lessons within a course.
  
- **Student Features:**
  - Enroll in courses.
  - View course content.
    

- **Security:**
  - Only instructors can manage their courses and lessons.
  - Only enrolled students can access course content.


## Used Technologies

- Language: Python
- Backend: Django
- Forntend: HTML, CSS
- Database: SQLite3

## Clone this project
   ```
   git clone https://github.com/emon51/Django_Project_OnlineLearningPlatform.git
   ```

## Setup Instructions

1. Create a new folder named 'GigaTech'
2. Open the folder 'Gigatech' in CMD
3. Install virtual-Environment (>pip install virtualenv)
4. Make a virtual environment named 'myenv' (>python -m virtualenv myenv)
5. Go to 'myenv' (>cd myenv) 
6. Go to 'myenv/Scripts' (>cd Scripts) 
7. Activate virtual environment 'myenv' (>activate) 
8. Install Django (>pip install django)
9. Back to 'myenv' folder (>cd ..)
10. Back to 'GigaTech' folder (>cd ..)
11. Check django version (>python -m django --version)
12. Start a project named 'OnlineLearningPlatform' (>django-admin startproject OnlineLearningPlatform)
13. Go to 'OnlineLearningPlatform' folder (>cd OnlineLearningPlatform)
14. Create an app into 'OnlineLearningPlatform' folder named 'courses' (>python manage.py startapp course)
15. Create a an another app into 'OnlineLearningPlatform' folder named 'users' (>python manage.py startapp users)
16. Run project on webserver (>python manage.py runserver)
17. Create a superuser:- username: emon, email: emon@gmail.com and password: emon
