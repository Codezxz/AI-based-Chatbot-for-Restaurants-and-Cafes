from django.contrib import admin
from django.urls import path
from src import views

urlpatterns = [
    path('', views.bill),

 
]
 