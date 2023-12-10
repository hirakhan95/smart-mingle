from django.db import models
from django.contrib.auth.models import AbstractUser


class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    venue = models.CharField(max_length=200)

    def __str__(self):
        return self.title




# class CustomUser(AbstractUser):
#     # add additional fields here if needed
#     pass