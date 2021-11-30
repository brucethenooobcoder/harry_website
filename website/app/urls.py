from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
 path('', views.root, name='rootpage'),
 path('home/', views.home, name='home'),
 path('about/', views.about, name='about'),
 path('services/', views.services, name='about'),

]