from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def handleLogin(request):
    if request.method=='POST':
        get_email=request.POST.get('email')
        get_password=request.POST.get('pass1')
        
        myUser=authenticate(username=get_email, password=get_password)
        if myUser is not None:
            login(request, myUser)
            # messages.success(request,'logged in successfully')
            return redirect('/')
        else:
            messages.error(request,'invalid credentials')
        
    return render(request, 'login.html')

def signup(request):
    
    if request.method == 'POST':
        get_fname=request.POST.get('fname')
        get_lname=request.POST.get('lname')
        get_email=request.POST.get('email')
        get_password =request.POST.get('pass1')
        get_confirm_password=request.POST.get('pass2')

        if get_password != get_confirm_password:
            messages.info(request,'Password not matching')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(email=get_email):
                messages.warning(request,'Email is taken')
                return redirect('/auth/signup/')
        except Exception as identifier:
            pass
        
        myUser=User.objects.create_user(get_email,get_email,get_password)
        myUser.save()
        
        myUser = authenticate(email=get_email,password=get_password)
        if myUser is not None:
            login(request, myUser)
            messages.success(request, 'user created & login success')
            return redirect('/')
    
    return render(request, 'signup.html')

def handleLogout(request):
    logout(request)
    messages.success(request,'Logout successful')
    return render(request, 'login.html')