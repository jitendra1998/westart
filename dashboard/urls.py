from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .views import StartUpListView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('viewstartup/', StartUpListView.as_view(), name='viewstartup')
]