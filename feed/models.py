from django.db import models

# Create your models here.

class Post(models.Model):
    text = models.CharField(max_length=250,blank=False)
    
    def __str__(self):
        return self.text
    