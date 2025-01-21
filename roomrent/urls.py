"""
URL configuration for roomrent project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from roombooking import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rooms/', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/<int:pk>/booking/', views.create_booking, name='create_booking'),
    path('room/<int:pk>/rental/', views.create_rental, name='create_rental'),

    path('register/', views.user_registration, name='user_registration'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),

    path('register_company/', views.register_company, name='register_company'),

    path('user/bookings/', views.user_bookings, name='user_bookings'),

    path('company/rentals/', views.company_rentals, name='company_rentals'),
    path('company/rooms/', views.company_rooms, name='company_rooms'),
]
