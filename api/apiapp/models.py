from django.db import models

# Create your models here.
class Employee(models.Model):
    eno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=30)
    esal=models.IntegerField()
    