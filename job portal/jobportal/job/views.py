from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



def index(request):
    return render(request,"index.html",)


def signin(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        user_name=request.POST['user_name']
        email=request.POST['email']
        password=request.POST['password']
        validpassword=request.POST['validpassword']
        if password==validpassword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"username taken")
                return redirect('index')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('index')
            else:
                user=User.objects.create_user(username=user_name,password=password,first_name=first_name,email=email,last_name=last_name)
                user.save()
                return render(request,"login.html")
        else:
            messages.info(request,"username taken")
            return redirect('index')
        return redirect('/') 
    else:    
        return render(request,"signin.html")
        
def login(request) :
        if request.method=='POST' :
            user_name=request.POST['user_name']
            password=request.POST['password']
            user=auth.authenticate(username=user_name,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,'invalid')
                return redirect('login')
        else :
            return render(request,'login.html')


