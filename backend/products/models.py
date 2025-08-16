
from django.db import models
class Product(models.Model):
    name=models.CharField(max_length=200)
    category=models.CharField(max_length=100, blank=True)
    bank=models.CharField(max_length=100, blank=True)
    def __str__(self): return self.name
