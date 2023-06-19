from Share.models import *
from django.contrib import admin

class shared_data(admin.ModelAdmin):
    list_display = ("id", "share_code", "user", "company", "last_viewed")
    
admin.site.register(Shared_data, shared_data)