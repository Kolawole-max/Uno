from company.models import *
from data_collection.models import *
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
import random
import string
from Share.models import *
from data_collection.models import *
from django.db import IntegrityError
import datetime
from verify.models import *

def get_logged_company(request):
    return Users.objects.get(id=request.user.id)

def get_company_det(request):
    user = get_logged_company(request=request)
    return user.company_user.get()

def if_company_exit(request):
    user = Users.objects.get(id=request.user.id)
    try: 
        Company.objects.get(user=user).exits()
    except Exception as e:
        raise PermissionDenied()
    

def get_string(letters_count, digits_count):
    letters = ''.join((random.choice(string.ascii_letters) for i in range(letters_count)))
    digits = ''.join((random.choice(string.digits) for i in range(digits_count)))

    # Convert resultant string to list and shuffle it to mix letters and digits
    sample_list = list(letters + digits)
    random.shuffle(sample_list)
    # convert list to string
    final_string = ''.join(sample_list)
    return final_string


# Create your views here.

def company_logout_view(request):
    logout(request)
    return redirect("adlogin")

def company_login_view(request):
    if request.method == "POST":
        
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect("admin_dashboard")
        else:
            return render(request, "company/login.html", {
                "message": 'Incorrect password'
            })
    else:
        return render(request, "company/login.html")
    
    
def company_register_view(request):
    if request.method == "POST":
        
        # Attempt to sign user in
        email = request.POST["email"]
        password = request.POST["password"]
        name = request.POST["name"]
        
          # Attempt to create new user
        try:
            user = Users.objects.create_user(username=email, email=email, password=password, age=50)
            user.save()
        except IntegrityError as e:
            error_message = str(e)
            print(error_message)
            return render(request, "company/login.html", {
                "message": "Username already taken."
            })
        login(request, user)

        user = Users.objects.get(id=request.user.id)
        company = Company.objects.create(user=user, name=name, verified=False, unique_id=get_string(5, 5))
        company.save()
        return redirect("admin_dashboard")
    else:
        return render(request, "company/login.html")
    
    
def company_dashboard(request):
    #if_company_exit(request=request)
    company = get_company_det(request=request)
    share_data = Shared_data.objects.filter(company=company.id).all()
   # searched_user = share_data.user.user_data
    return render(request, "company/dashboard.html", {
        'user_type' : "company",
        'company' : company,
        'share_dets' :share_data,
        #'searched_user' : searched_user
    })
    
def search_user(request):
    if request.method == "POST":
        
        name = request.POST["name"]
        share_code = request.POST["share_code"]
        
        share = Shared_data.objects.get(share_code=share_code)
        
        now = datetime.datetime.now()

        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        
        if share.company == None:
            share.company = get_company_det(request=request)
            
        else:
            if share.company != get_company_det(request=request):
                return render(request, 'company/search_user.html', {
                    'error' : "Share code didn't match query"
                })
        share.last_viewed = formatted_date
        share.save()
        data = share.user
        user = Users.objects.get(id=data.user.id)
        address = Address.objects.get(user=data.user.id)
        document = Documents.objects.filter(user=user)[:2]
        img = Saved_faces.objects.filter(user=user)
        display_img = img.first()
        return render(request, 'company/search_user.html', {
            'name' : data.firstname,
            'data' : data,
            'address' : address,
            'user_email' : user.email,
            'document' : document,
            'display_img' : display_img
        })
    else:
        return render(request, 'company/search_user.html')