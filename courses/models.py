from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Course(models.Model):
    title = models.CharField(max_length = 75)
    description = models.TextField()
    instructor = models.ForeignKey(User, on_delete = models.CASCADE)
    students = models.ManyToManyField(User, related_name = 'student_courses', blank = True)

    def __str__(self):
        return self.title
   
   


   
