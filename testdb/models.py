from django.db import models
# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    age = models.IntegerField()
# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    department = models.CharField(max_length=15)
    email = models.EmailField()
    phone = models.BigIntegerField()

