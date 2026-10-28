from django.db import models

# Create your models here.
class Student_data(models.Model):
    Fullname = models.CharField()
    Grade = models.IntegerField()
    Phone_number = models.CharField()
    

    