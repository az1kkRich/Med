from django.db import models
from distutils.command.upload import upload
from turtle import end_fill, title

# Create your models here.
class ServicesImg(models.Model):
    title = models.CharField( max_length=50)
    img = models.ImageField( upload_to='ServicesImg')

    def __str__(self):
        return self.title

class LatestBlog(models.Model):
    title = models.CharField( max_length=50)
    info = models.CharField( max_length=250)
    time = models.DateTimeField(auto_now=False, auto_now_add=False)
    img = models.ImageField( upload_to='BlogImg')

    def __str__(self):
        return self.title

class Member(models.Model):
    name = models.CharField( max_length=50)
    info = models.CharField( max_length=50)
    img = models.ImageField( upload_to='BlogImg')
    date = models.DateField(auto_now_add=True)

    # social
    telegram = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    name = models.CharField( max_length=50)
    info = models.CharField( max_length=50)
    img = models.ImageField( upload_to='BlogImg')

    def __str__(self):
        return self.name

class Page(models.Model):
    name = models.CharField( max_length=50)
    info = models.CharField( max_length=250)
    ixtisosi = models.CharField( max_length=50)
    summa = models.CharField( max_length=50)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name