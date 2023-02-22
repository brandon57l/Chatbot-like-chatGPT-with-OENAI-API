
from django.db import models
  
# Create your models here.
class Todo(models.Model):
    task = models.CharField(max_length=200)
  
    def __str__(self):
        return f"{self.task}"
    
class Message(models.Model):
    text = models.CharField(max_length=500)
    isClient = models.BooleanField(default=True)
    date = models.DateTimeField(auto_now=True)
  
    def __str__(self):
        return f"{self.text}"