from django.db import models
from data_collection.models import *
from company.models import *

# Create your models here.
    
class Shared_data(models.Model):
    share_code = models.CharField(max_length=64, blank=False, default=None)
    user = models.ForeignKey(Data, on_delete=models.CASCADE, blank=False, default=None, related_name='shared_user')
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True, default=None, related_name='shared_company')
    last_viewed = models.DateTimeField(default=None, blank=True, null=True)
    
    def __str__(self):
        return f" {self.company}"
    
    def serialize(self):
        return {
            'id' : self.id,
            'user' : self.user.id,
            'company' : self.user.name,
            'unique_id' : self.company.unique_id,
            'last_viewed': self.last_viewed
        }