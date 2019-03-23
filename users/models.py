from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class CandidateProfile(models.Model):
    user = models.OneToOneField(User, on_delete='CASCASDE')

    phone_number = models.CharField(max_length=12)
    ug_college = models.CharField(max_length=70)
    ug_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    pg_college = models.CharField(max_length=70, blank=True)
    pg_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True)
    work_exp = models.DecimalField(max_digits=2, decimal_places=0)
    resume = models.FileField(upload_to='users/resumes')

    def __str__(self):
        return self.user.username
