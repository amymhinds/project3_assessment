from django.db import models
from django.urls import reverse
# Create your models here.

class Wish(models.Model):
  wish = models.CharField(max_length=100, default = None)

  # def get_absolute_url(self):
  #   return reverse('wish_detail', kwargs={'wish_id': self.id})
