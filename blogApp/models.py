from django.db import models
from django.db.models.fields import related
from django.utils import timezone
from django.contrib.auth.models import User
# from django import forms

# Create your models here.

class Blog(models.Model):
    title= models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    description= models.CharField(max_length=100)
    date= models.DateTimeField()
    post= models.TextField(max_length=10000)
    image = models.ImageField(upload_to='Images')
    likes= models.IntegerField(default=0)
    dislikes= models.IntegerField(default=0)
    post_views = models.ImageField(default=0,null=True,blank=True)

    def __str__(self):
        return self.title
    @property
    def number_of_comments(self):
        return Comment.objects.filter(blogpost_connected=self).count()

class Comment(models.Model):
    post = models.ForeignKey(Blog,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
 
    # active = models.BooleanField(default=False)

   

    def __str__(self):
        return 'Comment {} by {}'.format(self.post.title, self.name)

class AboutSite(models.Model):
    name = models.CharField(max_length=100)
# class Like(models.Model):
#     likes =models.ManyToManyField( Blog,related_name='post_likes', blank=True,)

class Newsletter(models.Model):
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email
class Contactus(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Email Sent by {} On {}".format(self.name,self.timestamp)

class ProfileCard(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to="Profile/{}".format(name))
    facebook= models.URLField(blank=True)
    whatsapp = models.URLField(blank=True)
    insta = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    github = models.URLField(blank=True)
    linkedln = models.URLField(blank=True)

    def __str__(self):
        return  "{} a {}".format(self.name,self.title)