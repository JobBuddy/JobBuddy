from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='jobs-home'),
    path('candidate/', views.candidate, name='candidate'),
    path('cand_register/', views.cand_register, name='cand_register'),
    path('register/', views.register, name='register'),

    path('user_login/', views.user_login, name='user_login'),
    path('success/', views.success, name='success'),
    path('user_logout/', views.user_logout, name='user_logout'),
]
