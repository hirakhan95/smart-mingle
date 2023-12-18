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
    organizer = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=80, unique=True)
    img_url = models.CharField(max_length=250)
    description = models.TextField()
    location = models.CharField(max_length=50)
    category = models.CharField(max_length=15)
    start_time = models.DateTimeField()
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)


