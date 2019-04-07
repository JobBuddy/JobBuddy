from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name="app_home"),
    path('company_home', views.company_home, name="company_home"),
    path('company_login', views.company_login, name="company_login"),
    # path('company_logout', views.company_logout, name="company_logout"),
    path('company_logout', auth_views.LogoutView.as_view(template_name="accounts/home.html"), name="company_logout"),
    path('company_register', views.company_register, name="company_register"),
    path('company_profile', views.company_profile, name="company_profile"),
    path('company_forgetpassword', views.company_forgetpassword, name="company_forgetpassword"),


    path('freelancer_profile', views.freelancer_profile, name="freelancer_profile"),
    path('freelancer_login', views.freelancer_login, name="freelancer_login"),
    path('freelancer_register', views.freelancer_register, name="freelancer_register"),
    path('freelancer_home', views.freelancer_home, name="freelancer_home"),
    path('freelancer_forgetpassword', views.freelancer_forgetpassword, name="freelancer_forgetpassword"),
    #path('login/', views.user_login, name='login'),

    path('companyjobs', views.companyjobs, name='companyjobs'),

    path('recruiter_profile', views.recruiter_profile, name="recuiter_profile"),
    path('recruiter_login', views.recruiter_login, name="recruiter_login"),
    path('recruiter_register', views.recruiter_register, name="recruiter_register"),
    path('recruiter_home', views.recruiter_home, name="recruiter_home"),
    path('recruiter_forgetpassword', views.recruiter_forgetpassword, name="recruiter_forgetpassword"),

    path('candidate/', views.candidate, name='candidate'),
    path('cand_register/', views.cand_register, name='cand_register'),
    path('register/', views.register, name='register'),

    path('user_login/', views.user_login, name='user_login'),
    path('success/', views.success, name='success'),
    path('user_logout/', views.user_logout, name='user_logout'),


]
