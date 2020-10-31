from django.db import models
# from django import forms

# Create your models here.

class Blog(models.Model):
    title= models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    date= models.DateTimeField()
    post= models.TextField(max_length=10000)
    image = models.ImageField(upload_to='Images')

    def __str__(self):
        return self.title