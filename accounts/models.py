from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.forms import ModelForm, CharField, TextInput
from django.core.validators import URLValidator
from django.conf import settings


class User(AbstractUser):
    is_company = models.BooleanField(default=False)
    is_recruiter = models.BooleanField(default=False)
    is_freelancer = models.BooleanField(default=False)
    is_candidate = models.BooleanField(default=False)

class Company(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    # username = models.CharField(max_length=100, default='xyz')
    company_name = models.CharField(max_length=100)
    sector = models.CharField(max_length=100)
    website = models.TextField(validators=[URLValidator()])
    about = models.TextField()
    # password1 = models.CharField(max_length=100, default='hello123')
    # password2 = models.CharField(max_length=100, default='hello123')

class Recruiter(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    # Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    # Company_name = models.CharField(max_length=100)
    PAN = models.CharField(max_length=15)
    # password1 = models.CharField(max_length=100, default='hello123')
    # password2 = models.CharField(max_length=100, default='hello123')

class Jobs(models.Model):
    recruiter = models.ForeignKey(Recruiter, on_delete=models.CASCADE)
    CTC_from = models.CharField(max_length=100, default='1000000')
    CTC_to = models.CharField(max_length=100, default='100000')
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100, default='internship')
    Location = models.CharField(max_length=1000, default='Ranchi')
    Qualification = models.CharField(max_length=1000, default='BE')
    job_decription = models.TextField()
    min_exp = models.CharField(max_length=1000, default='less than one year')
    #author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_posted = models.DateTimeField(default=timezone.now)

class CandidateProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    jobs = models.ManyToManyField(Jobs)

    phone_number = models.CharField(max_length=12)
    ug_college = models.CharField(max_length=70)
    ug_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    pg_college = models.CharField(max_length=70, blank=True)
    pg_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    work_exp = models.DecimalField(max_digits=2, decimal_places=0)
    resume = models.FileField(upload_to='users/resumes')

    def __str__(self):
        return self.user.username

class Freelancer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True)
    candidate = models.ManyToManyField(CandidateProfile)
    #user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length=100)
    #image = models.ImageField(default='default.jpg',upload_to='profile_pics')
    Name = models.CharField(max_length=100)
    # Email = models.EmailField()
    Phone = models.CharField(max_length=15)
    Qualification = models.CharField(max_length=1000)
    Location = models.CharField(max_length=1000)
    PAN = models.CharField(max_length=15)
    # password1 = models.CharField(max_length=100, default='hello123')
    # password2 = models.CharField(max_length=100, default='hello123')
