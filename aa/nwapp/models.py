from django.db import models
from django.utils import timezone


# Create your models here.

class login(models.Model):
    userid = models.CharField(max_length=200)
    password = models.IntegerField()


class Registermodel(models.Model):
    firstname = models.CharField(max_length=300)
    lastname = models.CharField(max_length=200)
    userid = models.CharField(max_length=200)
    password = models.IntegerField()
    mblenum = models.BigIntegerField()
    email = models.EmailField(max_length=400, null=True)
    gender = models.CharField(max_length=200)


class Book_Details(models.Model):
    Book_Name = models.CharField(max_length=300)
    Author_Name = models.CharField(max_length=300)
    File_Data = models.FileField()
    Status = models.CharField(max_length=300)
    Create_Date = models.DateField(default=timezone.now)
    Update_Date = models.DateField(null=True)
