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
    path('register/', views.registration, name='registration'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('register_company/', views.register_company, name='register_company'),
    path('edit_company/<int:pk>/', views.edit_company, name='edit_company'),
    path('company/rooms/', views.company_rooms, name='company_rooms'),
    path('company/rentals/', views.company_rentals, name='company_rentals'),

    path('rooms/', views.room_list, name='room_list'),
    path('room/<int:pk>/', views.room_detail, name='room_detail'),
    path('room/<int:pk>/edit/', views.edit_room, name='edit_room'),
    path('create_room/', views.create_room, name='create_room'),

    path('room/<int:pk>/booking/', views.create_booking, name='create_booking'),
    path('room/<int:pk>/rental/', views.create_rental, name='create_rental'),
    path('user/bookings/', views.user_bookings, name='user_bookings'),

    path('dashboard/', views.dashboard, name='dashboard'),

    path('admin/', admin.site.urls),
]
