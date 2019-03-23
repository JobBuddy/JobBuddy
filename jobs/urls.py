from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('company/', views.company, name='jobs-company'),
]
