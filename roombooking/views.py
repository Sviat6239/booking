from django.shortcuts import render, get_object_or_404, redirect
from .models import Room, Booking, Rental
from .forms import BookingForm, RentalForm

def room_list(request):
    rooms = Room.objects.all()
    return render(request, 'roombooking/room_list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    return render(request, 'roombooking/room_detail.html', {'room': room})

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