from django.db import models

class Footer(models.Model):
    instagram = models.CharField(max_length=100)
    telegram = models.CharField(max_length=100)
    git = models.CharField(max_length=100)


class Message(models.Model):
    name = models.CharField(max_length=100)
    family = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    message = models.TextField()

def __str__(self):
    return self.name



