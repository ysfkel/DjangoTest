import datetime
from django.db import models
from django.utils import timezone


        
        
class Item(models.Model):
    name_text=models.CharField(max_length=50)
    def __str__(self):
        return self.name_text
    
