from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField()
    description = models.TextField()
    technologies = models.CharField() 
    link = models.URLField(blank=True)  
