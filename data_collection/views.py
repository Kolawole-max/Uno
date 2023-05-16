from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from data_collection.models import *
from django.db import IntegrityError
from django.conf import settings
import os
from django.views.decorators.csrf import csrf_exempt
from verify.views import *
from Share.models import *
from company.models import *
from verify.machinelearning import faces
from verify.models import Saved_faces
import json
import time
from django.core.serializers.json import DjangoJSONEncoder


# Create your views here.

def get_logged_user(request):
    return Users.objects.get(id=request.user.id)

def login_view(request):
    if request.method == "POST":
    
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("profile")
        else:
            return render(request, "data_collection/login.html", {
                "message": 'Incorrect password'
            })
    else:
        return render(request, "data_collection/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("login"))

def register(request):
    
    if request.method == "POST":
        
        email = request.POST['email']
        password = request.POST['password']
        
        #Attempt to create new user
        try:
            user = Users.objects.create_user(username=email, email=email, password=password, age=50)
            user.save()
            login(request, user)
            return redirect("create_data")
        
        except IntegrityError as e:
            error_message = str(e)
            print(error_message)
            return render(request, "data_collection/registration/reg_page1.html", {
                'message' : 'Email already exist',
                'email' : email,
                'password': password
            })
        
    else:
        return render(request, "data_collection/registration/reg_page1.html")
    
def create_data(request):
    
    if request.method == "POST":
    
        firstname = request.POST['first-name']
        lastname = request.POST['last-name']
        othername = request.POST['other-name']
        occupation = request.POST['occupation']
        contact_number = request.POST['contact-number']
        gender = request.POST['gender']
        marital_status = request.POST['marital']

        user = get_logged_user(request=request)
        
        data = Data.objects.create(
            user = user,
            firstname=firstname,
            lastname = lastname,
            othername = othername, 
            occupation = occupation,
            contact_number = contact_number,
            gender = gender, 
            marital_status = marital_status
        )
        data.save()
        return redirect('address_data')
    else:
        return render(request, "data_collection/registration/reg_page2.html")
    
def address_data(request):
    
    if request.method == "POST":
        
        house_number = request.POST['home-number']
        street = request.POST['street-name']
        city = request.POST['city']
        postal_code = request.POST['postal-code']
        home_town = request.POST['home-town']
    
        address_ = Address.objects.create(
            user = get_logged_user(request=request),
            house_number=house_number,
            street = street,
            city = city, 
            postal_code = postal_code,
            home_town = home_town
        )
        address_.save()
        return redirect('documents_')
    else:
        return render(request, "data_collection/registration/reg_page3.html")
    
def documents_(request):
    
    if request.method == "POST":
        # counters = [g
        try:
            images = request.FILES.getlist('identification-card')
            #faces(images=images)
            
            image_path = r'C:/Users/kolaw/OneDrive/Pictures/pics/kola.jpg'
    
            with open(image_path, 'rb') as f:
                image_data = f.read()
                
            image_name = os.path.basename(image_path)
            image_file = ContentFile(image_data)
            default_storage.save(image_name, image_file)
            
            saved_face = Saved_faces.objects.create(user=get_logged_user(request=request), faces=image_name)
            saved_face.save()

            #SaveImageFace(request=request, images=images)
            
            for image in images:
                documents = Documents.objects.create(user=get_logged_user(request=request), doc=image)
                documents.save()
                
            return redirect('verify')
        
        except IntegrityError as e:
            error_message = str(e)
            return render(request, "data_collection/registration/reg_page4.html", {
                "message": error_message
            })
    else:
        return render(request, "data_collection/registration/reg_page4.html")
    
    
def verify_(request):
    
    if request.method == 'POST':
        return redirect('profile')
    else:
        user = get_logged_user(request=request)
        documents_ = Documents.objects.filter(user=user)[:1]
        
        return render(request, "data_collection/registration/reg_page5.html", {
            "image_url" : documents_
        })
    
    
@csrf_exempt
def save_code(request):
    
    if request.method == 'POST':
        
        data = json.loads(request.body)
        code = data.get('code', '')
        
        user = Users.objects.get(id=request.user.id)
        user_data = Data.objects.get(user=user.id)
        share = Shared_data.objects.create(share_code=code, user=user_data)
        share.save()
        
        return JsonResponse({"message": "Share code created successfully."}, status=201)
    else:
        return JsonResponse({"message": "Error request code"}, status=404)   
  
        
def profile(request):
    
    user = get_logged_user(request=request)
    data = Data.objects.get(user=user)
    address = Address.objects.get(user=user)
    doc = Documents.objects.filter(user=user)
    saved_faces = Saved_faces.objects.filter(user=user)
    img = saved_faces.first()
    shared_det = data.shared_user.all()
    
    return render(request, 'data_collection/user-dashboard.html', {
        'user_type' : "user",
        'user' : user,
        'data': data,
        'address': address,
        'doc': doc,
        'share_dets' : shared_det,
        'img' : img
    })



#### API ######

def documents_api(request):
    user = get_logged_user(request=request)
    documents_ = Documents.objects.filter(user=user)
    # for document in documents_:
    #     my_object = [
    #         { 'user' : [str(document.user)]},
    #         { 'image': [str(document.doc)]}
    #     ]

    # json_data = json.dumps(my_object, cls=DjangoJSONEncoder)
    #return JsonResponse(json_data, safe=False)
    return JsonResponse([documents_.serialize() for documents_ in documents_], safe=False)



    