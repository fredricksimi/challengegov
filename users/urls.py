from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    path('accounts/signup/', views.MySignUpView.as_view(), name='account_signup'),
    path('accounts/login/', views.MyLoginView.as_view(), name='account_login'),
    ]
