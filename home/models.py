from django.db import models
# from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.email} - {self.phone} - {self.date}'
    
class Signup(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    confirm_password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.email} '
    
##########################################################################################
    
class Insta(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.username} - {self.password} '

