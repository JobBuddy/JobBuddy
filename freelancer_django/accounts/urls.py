from django.urls import path
from .views import register

from . import views

app_name="accounts"
urlpatterns = [
    path('signup/', views.register, name='register'),
    path('home/', views.home, name="home"),
    path('login/',views.user_login,name='login'),
]