from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # Login and Register Route
    path('login/', views.userLogin, name="user-login"),
    path('register/', views.userRegister, name="user-register"),
    path('logout/', views.userLogout, name='user-logout'),
    path('my-account/', views.userAccount, name= 'my-account'),

    #User Account Route
    path('my-account/', views.userAccount, name="user-account"),
    ]