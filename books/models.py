from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Book(models.Model):     
    title = models.CharField(max_length=200)     
    author = models.CharField(max_length=200)     
    isbn = models.CharField(max_length=13, unique=True)     
    published_date = models.DateField()    
    pages = models.IntegerField()     
    description = models.TextField(blank=True)     
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='books')    
    created_at = models.DateTimeField(auto_now_add=True)     
    updated_at = models.DateTimeField(auto_now=True)   
           
class Meta:         
    ordering = ["-created_at"]       

def __str__(self):         
    return f"{self.title} by {self.author}"
