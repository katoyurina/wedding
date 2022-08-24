from django.db import models

# Create your models here.
class Select(models.Model):
    name = models.CharField(max_length=100)    
    categoly_Choice = models.CharField(max_length=100)
    num_Choice = models.CharField(max_length=100)