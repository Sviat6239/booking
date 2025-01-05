from django import forms
from .models import Booking, Rental

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['start_date', 'end_date', 'total_cost']

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['rental_date', 'cost']