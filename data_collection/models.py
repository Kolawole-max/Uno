from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here. self.timestamp.strftime("%b %#d %Y, %#I:%M %p")

class Users(AbstractUser):
    age = models.CharField(max_length=64, blank=True, null=True, default=None)
    
    def __str__(self):
        return f" {self.id}"
    
    def serialize(self):
        return {
            'id' : self.id,
            'email' : self.email
        }

class Data(models.Model):                                                                         
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False, default=None, related_name="user_data")
    firstname = models.CharField(max_length=64, blank=False, default=None)
    lastname = models.CharField(max_length=64, blank=False, default=None)
    othername = models.CharField(max_length=64, blank=True)
    occupation = models.CharField(max_length=64, blank=True)
    contact_number = models.CharField(max_length=64, blank=True)
    gender = models.CharField(max_length=64, blank=True)
    marital_status = models.CharField(max_length=64, blank=True)
    
    def __str__(self):
        return f" {self.lastname} {self.firstname}"
    
    def serialize(self):
        return {
            'id' : self.id,
            'user' : self.user.id,
            'firstname' : self.firstname,
            'lastname' : self.lastname,
            'othername' : self.othername,
            'occupation' : self.occupation,
            'contact_number' : self.contact_number,
            'gender' : self.gender,
            'marital_status' : self.marital_status
        }


    
    
class Address(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    house_number = models.CharField(max_length=64, blank=False)
    street = models.CharField(max_length=64, blank=False)
    city = models.CharField(max_length=64, blank=False)
    postal_code = models.CharField(max_length=64, blank=False)
    home_town = models.CharField(max_length=64, blank=False)
    
    def serialize(self):
        return {
            'id' : self.id,
            'user' : self.user.id,
            'house_number' : self.house_number,
            'street' : self.street,
            'city' : self.city,
            'postal_code' : self.postal_code,
            'home_town' : self.home_town
        }
    
class Documents(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE, blank=False)
    doc = models.FileField(null=True, blank=True)

    def serialize(self):
        return {
            'id' : self.id,
            'user' : self.user.email,
            'doc' :  str(self.doc)
        }
        