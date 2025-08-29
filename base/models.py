from django.db import models


class Category (models.Model):
    name=models.CharField(max_length=200)
    description=models.TextField(blank=True)


class Profile(models.Model):
    name=models.CharField(max_length=200)
    phone=models.CharField(max_length=200, blank= True)
    bio=models.TextField(blank=True)
    profile_picture=models.ImageField(upload_to='profiles/', blank=True, null=True)
    


class Priority(models.Model):
    title=models.CharField(max_length=200)
    level=models.CharField(max_length=200)



class Task(models.Model):
    title=models.CharField(max_length=200)
    description=models.CharField(max_length=200 , blank=True,)
    created_at=models.DateField(auto_now_add=True )
    due_date=models.DateField(null=True , blank=True)
    completed = models.BooleanField(default=False)
    category=models.ForeignKey(Category, on_delete=models.SET_NULL , null=True , blank= True)
    priority=models.ForeignKey(Priority , on_delete=models.SET_NULL , null=True , blank=True)



