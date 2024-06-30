from django.db import models

class Student(models.Model):
    studentId = models.CharField(max_length=12)
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=10)
