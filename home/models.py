from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100,blank=False,null=False)
    email=models.EmailField()
    age=models.CharField(max_length=10,blank=False)
    gender=models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name
    