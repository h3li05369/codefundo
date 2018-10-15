from django.db import models
from django import forms


# Create your models here.


class LogIn(models.Model):

    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)


    def __str__(self):
        return self.email

class Graphs(models.Model):

    Graph_Type = models.CharField(max_length=100)
    Graph_description = models.TextField(max_length=1000)
    Graph_Algorithms = models.TextField(max_length=1000)


    def __str__(self):
        return self.Graph_Type
