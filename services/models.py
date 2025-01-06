from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title

class Options(models.Model):
    title = models.CharField(max_length=120)
    def __str__(self):
        return self.title
    
class Services(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to="service",default="default.jpg")
    desc = models.TextField()
    category = models.ManyToManyField(Category)
    options = models.ManyToManyField(Options)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Features(models.Model):
    title = models.CharField(max_length=120)
    content = models.CharField(max_length=120)
    image = models.ImageField(upload_to="service",default="default.jpg")
    options = models.ManyToManyField(Options)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.title 
