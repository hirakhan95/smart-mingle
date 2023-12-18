from django.db import models
from django.contrib.auth.models import User
from django.db import models


class ExtraDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    phone_num = models.CharField(max_length=20)
    display_pic = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)


class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone_number = models.CharField(max_length=20)
    description = models.CharField(max_length=150)


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.title