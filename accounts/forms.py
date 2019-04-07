from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from .models import Company, Freelancer, Jobs, Recruiter
from django.forms import ModelForm
from .models import CandidateProfile
from django.db import transaction


User = get_user_model()

class CompanyRegisterForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Username', 'aria-hidden': "true"}))
    # company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'eg. OLA', 'aria-hidden': "true"}))
    # Sector = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'eg. IT'}))
    # Website = forms.URLField(widget=forms.URLInput(attrs={'class': 'form-control input', 'placeholder': 'eg. https://www.olacabs.com/'}))
    # #Phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Phone'}))
    # #Qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Qualification'}))
    # #Location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Location'}))
    # #PAN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'PAN'}))
    # About = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Company
        fields = ["company_name", "sector", "website", "about"]

    # @transaction.atomic
    # def save(self):
    #    user = super().save(commit=False)
    #    user.is_company = True
    #    user.save()
    #    return user


class RecruiterRegisterForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Username', 'aria-hidden': "true"}))
    # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Name'}))
    # Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control input', 'placeholder': 'Email'}))
    # Phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Phone'}))
    # company_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'eg. OLA', 'aria-hidden': "true"}))
    # PAN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'PAN'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model =  Recruiter
        fields = ["Name", "Phone", "Company_name", "PAN"]
    #
    # @transaction.atomic
    # def save(self):
    #    user = super().save(commit=False)
    #    user.is_recruiter = True
    #    user.save()
    #    return user


class FreelancerRegisterForm(forms.ModelForm):
    # username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Username', 'aria-hidden': "true"}))
    # Name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Name'}))
    # Email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control input', 'placeholder': 'Email'}))
    # Phone = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Phone'}))
    # Qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Qualification'}))
    # Location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'Location'}))
    # PAN = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': 'PAN'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control input', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = Freelancer
        fields = ["Name", "Phone", "Qualification", "Location", "PAN"]

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_freelancer = True
    #     user.save()
    #     return user


class CompanyJobsForm(forms.ModelForm):
    # CTC_from = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control input', 'placeholder': '', 'aria-hidden': "true"}))
    # CTC_to = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control input', 'placeholder': ''}))
    # job_title = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # company = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # job_type = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # Location = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # Qualification = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # job_decription = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))
    # min_exp = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'class': 'form-control input', 'placeholder': ''}))
    # #author = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_posted = forms.DateTimeField(widget=forms.TextInput(attrs={'class': 'form-control input', 'placeholder': ''}))

    class Meta:
        model = Jobs
        fields = ["CTC_from", "CTC_to", "job_title", "company", "job_type", "Location", "Qualification", "job_decription", "min_exp", "date_posted"]


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class CandidateProfileForm(forms.ModelForm):
    class Meta():
        model = CandidateProfile
        fields = ('phone_number', 'ug_college', 'ug_percentage', 'pg_college', 'pg_percentage', 'work_exp', 'resume')

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_candidate = True
    #     user.save()
    #     return user


# class SearchForm(forms.Form):
#     job_title = forms.CharField(max_length=100)
