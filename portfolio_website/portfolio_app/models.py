from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.TextField(max_length=200)
    technologies = models.CharField(max_length=100) 
    link = models.URLField(blank=True)  
