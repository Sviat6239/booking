from datetime import date

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Room, Booking, Rental, Company
from .forms import BookingForm, RentalForm, CompanyForm, CustomUserCreationForm, CustomUserLoginForm

def index(request):
    return render(request, 'roombooking/index.html')

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'roombooking/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'roombooking/room_detail.html', {'room': room})

@login_required
def create_booking(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.room = room
            booking.user = request.user
            booking.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = BookingForm()
    return render(request, 'roombooking/booking_form.html', {'form': form})

@login_required
def create_rental(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == 'POST':
        form = RentalForm(request.POST)
        if form.is_valid():
            rental = form.save(commit=False)
            rental.room = room
            rental.user = request.user
            rental.save()
            return redirect('room_detail', pk=room.pk)
    else:
        form = RentalForm()
    return render(request, 'roombooking/rental_form.html', {'form': form})

def registration(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            messages.success(request, f'Welcome {user.username}! You have been successfully registered.')
            return redirect('index')
        else:
            messages.error(request, 'Registration failed. Please check the form for errors.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'roombooking/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomUserLoginForm(request, data=request.POST)
        if form.is_valid():
            print("Form is valid")
            user = form.get_user()
            auth_login(request, user)
            messages.success(request, f'Welcome back, {user.username}!')
            return redirect('index')
        else:
            print("Form is not valid")
            print(form.errors)
            messages.error(request, 'Invalid username or password.')
    else:
        form = CustomUserLoginForm()
    return render(request, 'roombooking/login.html', {'form': form})

def logout(request):
    auth_logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('index')

@login_required
def register_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your company has been successfully registered.')
            return redirect('index')
        else:
            messages.error(request, 'Company registration failed. Please check the form for errors.')
    else:
        form = CompanyForm(user=request.user)
    return render(request, 'roombooking/company_registration.html', {'form': form})

@login_required
def company_rooms(request):
    company = get_object_or_404(Company, owner=request.user)
    rooms = company.rooms.all()

    room_status = []
    for room in rooms:
        booking_exists = Booking.objects.filter(room=room, end_date__gte=date.today()).exists()
        rental_exists = Rental.objects.filter(room=room, rental_date__gte=date.today()).exists()

        room_status.append({
            'room': room,
            'is_booked': booking_exists or rental_exists,
        })

    return render(request, 'roombooking/company_rooms.html', {'room_status': room_status})

@login_required
def user_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'roombooking/user_bookings.html', {'bookings': bookings})

@login_required
def company_rentals(request):
    company = get_object_or_404(Company, owner=request.user)
    rentals = Rental.objects.filter(room__company=company)
    return render(request, 'roombooking/company_rentals.html', {'rentals': rentals})

@login_required
def dashboard(request):
    user = request.user
    return render(request, 'roombooking/dashboard.html', {'user': user})