from django.shortcuts import render,redirect
import requests as req
from login.models import UserLogin
from django.contrib.auth.models import auth, User
from django.contrib import messages
import re

# Create your views here.
def login(request):
    return render(request,"login.html")

def memepage(request):
    isAuthorized=False
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        
        if len(username)==0:
            messages.error(request,'username can not be empty')
            return redirect("login")
        if len(password)==0:
            messages.error(request,'password can not be empty')
            return redirect("login")
        if len(password)>8:
            messages.error(request,'password can not be more than 8 characters')
            return redirect("login")
        if not re.match("[A-Za-z0-9@_]", str(password)):
            messages.error(request,'password does not matches the requirements')
            messages.info(request,'Please give a lowecase letter, an uppercase letter, a digit and special character and should be less than 8 characters')
            return redirect("login")
            
        user=auth.authenticate(username=username,password=password)
        # for name,passs,cookie in UserLogin.objects.all():
        #     if name==username and passs==password:
        #         isAuthorized=True
        #         break
        
        if user is not None:
            auth.login(request, user)
            x=request.COOKIES
            return render(request,"userpage.html",{'cookies':x})  
        else:
            messages.error(request,'invalid credentials')
            return redirect("login")
    else:
        return render(request,"login.html")
    

def logout(request):
    auth.logout(request)
    return redirect('login')

def showmemes(request):
    url="https://api.imgflip.com/get_memes"
    resp=req.get(url)
    resp=resp.json()
    memelist=resp["data"]["memes"][:6]
    return render(request,"home.html",{'meme':memelist})