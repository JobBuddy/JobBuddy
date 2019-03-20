from django import forms
from django.contrib.auth.models import User
#from django.contrib.auth.forms import UserCreationForm
from .models import Users
from django.forms import ModelForm

class UserRegisterForm(ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'Username','aria-hidden':"true"}))
	Name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'Name'}))
	Email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control input','placeholder':'Email'}))
	Phone = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'Phone'}))
	Qualification = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'Qualification'}))
	Location = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'Location'}))
	PAN = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control input','placeholder':'PAN'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input','placeholder':'Password'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control input','placeholder':'Confirm Password'}))
	class Meta:
		model=Users
		fields=["username","Name","Email","Phone","Qualification","Location","PAN","password1","password2"]
	
		

# class ClassName(forms.ModelForm):
# 	#Name = forms.CharField(max_length=100)
# 	#Email = forms.EmailField()
# 	#Phone = forms.CharField(max_length=15)
# 	#Qualification = forms.CharField(max_length=1000)
# 	#Location = forms.CharField()
# 	#PAN = forms.CharField()
# 	password1 = forms.CharField(widget=forms.PasswordInput)
# 	password2 = forms.CharField(widget=forms.PasswordInput)
# 	class Meta:
# 		model = Users
# 		fields = [ 'Name','Phone','Qualification','Location','PAN',]
