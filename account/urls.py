from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

from account import views

urlpatterns = [
    path('account/register/sender/', views.SenderRegisterView.as_view()),
    path('account/register/buyer/', views.BuyerRegisterView.as_view()),
    path('account/login/', views.LoginView.as_view()),

]
