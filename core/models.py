from django.db import models
from authentication.models import User
from django.utils import timezone


class Course(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)
    course_image = models.ImageField(upload_to='media')
    teacher_name = models.CharField(max_length=50)
    teacher_details = models.TextField()
    course_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    end_date = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name


class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    marks = models.CharField(max_length=20)
    duration = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class AssignmentSubmission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ass = models.ManyToManyField(Assignment,related_name='assignments')#//Try one to one field
    name = models.CharField(max_length=100)
    university_id = models.CharField(unique=True,max_length=100)
    file = models.FileField(upload_to='media')

    def __str__(self):
        return self.university_id 

class AssignmentResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # ass_sub = models.ManyToManyField(AssignmentSubmission,related_name='asss')#//Try one to one field  # user_id=models.ForeignKey(User.id, on_delete=models.DO_NOTHING ,null=True)
    marks = models.CharField(max_length=10)
    comments = models.TextField(null=True,blank=True)
    file = models.FileField(upload_to='media/studReport')
  
 