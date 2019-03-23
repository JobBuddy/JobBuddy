from django import forms
from django.contrib.auth.models import User
from .models import CandidateProfile

class  UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class CandidateProfileForm(forms.ModelForm):
    class Meta():
        model = CandidateProfile
        fields = ('phone_number', 'ug_college', 'ug_percentage', 'pg_college', 'pg_percentage', 'work_exp', 'resume')
