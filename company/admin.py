from company.models import *
from django.contrib import admin

class company(admin.ModelAdmin):
    list_display = ("id", "name", "unique_id", "verified")
    
admin.site.register(Company, company)