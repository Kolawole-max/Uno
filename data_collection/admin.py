from data_collection.models import *
from django.contrib import admin


class users(admin.ModelAdmin):
    list_display = ("id", "email", "password")
    
class data(admin.ModelAdmin):
    list_display = ("id", "user", "firstname", "lastname", "othername", "occupation", "contact_number", "gender", "marital_status")
    
class address(admin.ModelAdmin):
    list_display = ("id", "user", "house_number", "street", "city", "postal_code", "home_town")
    
class documents(admin.ModelAdmin):
    list_display = ("id", "user", "doc")
    
admin.site.register(Users, users)
admin.site.register(Data, data)
admin.site.register(Address, address)
admin.site.register(Documents, documents)