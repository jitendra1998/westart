from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.signup, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/', views.login, name='login'),
    path('logout/',views.logout, name = 'logout'),
    path('userorder/', views.userorder, name='userorder'),
    path('createstartup/', views.createstartup, name='createstartup'),
    path('viewallstart/', views.viewallstart, name='viewallstart'),
    path('showmenu/', views.showmenu, name='showmenu'),
    path('viewstartup/', views.StartUpListView, name='viewstartup'),
    path('userorder12/', views.userorder12, name='userorder12'),
    path('userprofile/', views.userprofile, name='userprofile'),

]
