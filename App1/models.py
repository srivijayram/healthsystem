from django.db import models


# Create your models here.
class Registeration(models.Model):  # step 5 need to creaet all fields and insert html file in templates
    name = models.CharField(max_length=50)  # create a new file urls.py in appname
    email = models.CharField(max_length=50, primary_key=True)
    password = models.CharField(max_length=8)


class Patient(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    phno = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    adhar = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=30)


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.CharField(max_length=50, unique=True)
    phno = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    lisence = models.CharField(max_length=12, primary_key=True)
    password = models.CharField(max_length=30)


class Messages(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    subject = models.CharField(max_length=100)
    text = models.CharField(max_length=250)

class Document(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    #file = models.FileField(upload_to='uploadfiles/')
    file = models.FileField()
    transactiontime = models.DateTimeField()

class Documents(models.Model):
    sender = models.CharField(max_length=50)
    receiver = models.CharField(max_length=50)
    #file = models.FileField(upload_to='uploadfiles/')
    file = models.FileField()
    transactiontime = models.DateTimeField()


class UserProfile(models.Model):

    name = models.CharField(max_length=25)
    email = models.EmailField(unique=True)
    type = models.CharField(max_length=25)


    def __str__(self):
        return f"{self.name}"