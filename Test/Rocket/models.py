from django.db import models

# Create your models here.

class AR(models.Model):
    name=models.CharField(max_length=255)
class Batch(models.Model):
    Batch=models.CharField(max_length=255)
    def __str__(self):
        return self.Batch
class Student(models.Model):
    Student=models.CharField(max_length=255)
    Batch=models.ForeignKey(Batch,on_delete=models.CASCADE)