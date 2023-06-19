from django.contrib import admin
from verify.models import *
from django.contrib import admin

class saved_faces(admin.ModelAdmin):
    list_display = ("id", "user", "faces")
    
admin.site.register(Saved_faces, saved_faces)
# admin.site.register(Image)