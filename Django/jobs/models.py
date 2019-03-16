from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.forms import ModelForm, CharField, TextInput


class Jobs(models.Model):
    salary = CharField(widget=TextInput(attrs={'type': 'number'}))
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_decription = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)
