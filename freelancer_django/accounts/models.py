from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
	#user = models.OneToOneField(User, on_delete=models.CASCADE)
	username = models.CharField(max_length=100)
	Name = models.CharField(max_length=100)
	Email = models.EmailField()
	Phone = models.CharField(max_length=15)
	Qualification = models.CharField(max_length=1000)
	Location = models.CharField(max_length=1000)
	PAN = models.CharField(max_length=15)
	password1 = models.CharField(max_length=100,default='hello123')
	password2 = models.CharField(max_length=100,default='hello123')
	def __str__(self):
		return self.id