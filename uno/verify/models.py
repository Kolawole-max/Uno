from django.db import models
from data_collection.models import *

# Create your models here.

class Saved_faces(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    faces = models.FileField(null=True, blank=True)

    