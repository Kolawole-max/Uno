from django.db import models
from data_collection.models import *

# Create your models here.

class Company(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, default=None, related_name="company_user")
    name = models.CharField(max_length=64, blank=False, default=None)
    unique_id = models.CharField(max_length=64, blank=False, default=None)
    verified = models.BooleanField(default=False, blank=False)
    
    def __str__(self):
        return f" {self.name}"
