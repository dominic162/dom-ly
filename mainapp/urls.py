from django.urls import path,include
from django.contrib import admin
from mainapp import views as mviews
from auth import views as aviews

urlpatterns = [
    path('login',aviews.auth_login,name="login"),
    path('logout',aviews.auth_logout,name="logout"),
    path('',mviews.dashboard,name="dashboard"),
    path('<str:query>',mviews.redr),
]