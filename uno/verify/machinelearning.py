import numpy as np
import cv2
import sklearn
import pickle
from django.conf import settings 
import os
import face_recognition
import dlib
from django.db import IntegrityError

from django.shortcuts import render
from django.http import HttpResponse
from verify.models import *
from data_collection.models import *
from django.db import IntegrityError

    


detector = dlib.get_frontal_face_detector()
new_path ='C:/Users/kolaw/OneDrive/Pictures/'



#new_path = 'verify/static/images/kay.jpeg'

def MyRec(rgb,x,y,w,h,v=20,color=(200,0,0),thikness =2):
    """To draw stylish rectangle around the objects"""
    cv2.line(rgb, (x,y),(x+v,y), color, thikness)
    cv2.line(rgb, (x,y),(x,y+v), color, thikness)

    cv2.line(rgb, (x+w,y),(x+w-v,y), color, thikness)
    cv2.line(rgb, (x+w,y),(x+w,y+v), color, thikness)

    cv2.line(rgb, (x,y+h),(x,y+h-v), color, thikness)
    cv2.line(rgb, (x,y+h),(x+v,y+h), color, thikness)

    cv2.line(rgb, (x+w,y+h),(x+w,y+h-v), color, thikness)
    cv2.line(rgb, (x+w,y+h),(x+w-v,y+h), color, thikness)

def save(img,name, bbox, width=180,height=227):
    print("Heloooooooo yes im working you fuckers")
    x, y, w, h = bbox
    imgCrop = img[y:h, x: w]
    imgCrop = cv2.resize(imgCrop, (width, height))#we need this line to reshape the images
    
    # user = Users.objects.get(id=request.user.id)
    # save_face = Saved_faces.objects.create(user=user, faces=imgCrop)
    # save_face.save()
    cv2.imwrite(name+".jpg", imgCrop)
    
    # img = cv2.imread(imgCrop)
    
    # retval, buffer = cv2.imencode('.jpg', img)
    # byte_string = buffer.tobytes()
    
    
    # doc = Documents.objects.create(user=Users.objects.get(id=1), doc=imgCrop)
    # doc.save()
    
    # saved_faces = Saved_faces.objects.create(user=Users.objects.get(id=1), faces=imgCrop)
    # saved_faces.save()
    

def faces(images):
    try:
        
        for image in images:
            filename = image.name                
            frame = cv2.imread(filename)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
            faces = detector(bgr)
            if faces is None and len(faces) > 0:
                print("No faces detected in image:")
            else:
                fit = 20
                
                for counter,face in enumerate(faces):
                    x1, y1 = face.left(), face.top()
                    x2, y2 = face.right(), face.bottom()
                    cv2.rectangle(frame,(x1,y1),(x2,y2),(220,255,220),1)
                    MyRec(frame, x1, y1, x2 - x1, y2 - y1, 10, (0,250,0), 3)
                    #cv2.imshow('img', gray)
                    print("Heloooooooo yes im working you fuckers")
                    save(gray,new_path+str(counter),(x1-fit,y1-fit,x2+fit,y2+fit)) # -- Saves bigger img
                    #save(gray,new_path+str(counter),(x1,y1,x2,y2))
                    
            #frame = cv2.resize(frame,(800,800))
                    
    except Exception as e:
        saveface_counter = 0
    
    #return saveface_counter
        
    