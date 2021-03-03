from django.contrib import admin
from django.urls import path
from auth import views

urlpatterns = [
    path('',views.auth,name="login"),
    path('logout',views.auth_logout,name="logout")
]
