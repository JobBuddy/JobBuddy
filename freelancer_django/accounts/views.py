from django.shortcuts import render,redirect
#from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.models import User


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            usernam = form.cleaned_data.get('username')
            pass1 = form.cleaned_data.get('password1')
            pass2 = form.cleaned_data.get('password2')
            if pass1 != pass2:
                raise forms.ValidationError('Password do not match.')
            if len(pass1)<8:
                raise forms.ValidationError('Minimum length of password should be 8.')
            form.save()
            # messages.success(request, f'Account created for {usernam}!')
            return render(request, 'accounts/login.html', {})
    else:
        form = UserRegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def home(request):
	return render(request, 'accounts/home.html', {})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        # data=request.POST.copy()
        # name = data.get('username')
        # pwd = data.get('password')
        # if name==username and pwd==password:
        # if username and password:
        # 	user = User.objects.get(username=username)
        # 	if user:
        # 		return HttpResponse("Successfully logged in")
        # else:
        # 	return HttpResponse("Invalid credentials")
        if user:
            login(request,user)
            return HttpResponse("Successfully logged in")
        else:
            return HttpResponse("Invalid login details given")
    
    return render(request, 'accounts/login.html')