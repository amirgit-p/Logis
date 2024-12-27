from django.db import models

from django.contrib.auth.models import User





class Job(models.Model):
    name = models.CharField(max_length=120)
    def __str__(self):
        return self.name


class CountStars(models.Model):
    count = models.IntegerField(default=5)
    def __str__(self):
        return str(self.count)

    

class Testimonials(models.Model):
    name = models.CharField(max_length=120)
    image = models.ImageField(upload_to="Agents",default="default.jpg")
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    stars = models.ForeignKey(CountStars,on_delete=models.DO_NOTHING)
    comment = models.TextField()
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name
    
    def stars_count(self):
        return range(self.stars.count)
    


class Agent(models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    job = models.ForeignKey(Job,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Agents",default="default.jpg")
    bio = models.TextField()
    instagram = models.CharField(max_length=120)
    facebook = models.CharField(max_length=120)
    linkedin = models.CharField(max_length=120)
    twitter = models.CharField(max_length=120)
    craeted_at = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    def __str__(self):
        return self.name

class Fqa(models.Model):
    questin = models.TextField()
    answer = models.TextField()