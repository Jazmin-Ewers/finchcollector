from django.db import models
from django.urls import reverse

# Create your models here.
class Finch(models.Model):
  species = models.CharField(max_length=100)
  population = models.CharField(max_length=100)
  habitat = models.TextField(max_length=250)
  threats = models.TextField(max_length=250)
  
  def __str__(self):
    return self.name
    
  def get_absolute_url(self):
    return reverse('finches_detail', kwargs={'finch_id': self.id})

    

