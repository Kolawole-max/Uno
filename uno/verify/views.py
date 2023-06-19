from django.shortcuts import render
from django.http import HttpResponse
from verify.models import *
from data_collection.models import *
from django.db import IntegrityError
from verify.machinelearning import *
from PIL import Image
import io
from django.core.files.base import ContentFile

import os
from django.core.files.storage import default_storage
# Create your views here.

def get_logged_user(request):
    return Users.objects.get(id=request.user.id)

def SaveImageFace(request, images):
    
    faces(images=images)
    
    