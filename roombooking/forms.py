from django import forms
from .models import Booking, Rental, Room, Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['room', 'start_date', 'end_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(company__owner=user)

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date and end_date:
            if end_date <= start_date:
                raise forms.ValidationError("End date must be after the start date.")
        return cleaned_data

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        room = cleaned_data.get('room')
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        total_cost = (end_date - start_date).days * room.cost_per_day
        instance = super().save(commit=False)
        instance.total_cost = total_cost
        instance.user = kwargs.get('user')
        instance.save()
        return instance

class RentalForm(forms.ModelForm):
    class Meta:
        model = Rental
        fields = ['room', 'rental_date', 'cost']
        widgets = {
            'rental_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super().__init__(*args, **kwargs)
        self.fields['room'].queryset = Room.objects.filter(company__owner=user)

    def clean(self):
        cleaned_data = super().clean()
        rental_date = cleaned_data.get('rental_date')

        if rental_date and rental_date < forms.DateInput().input_formats[0]:
            raise forms.ValidationError("Rental date cannot be in the past.")
        return cleaned_data

    def save(self, *args, **kwargs):
        cleaned_data = self.cleaned_data
        room = cleaned_data.get('room')
        rental_date = cleaned_data.get('rental_date')
        cost = room.cost_per_day
        instance = super().save(commit=False)
        instance.cost = cost
        instance.user = kwargs.get('user')
        instance.save()
        return instance

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address', 'contact_email']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.owner = self.user
        if commit:
            instance.save()
        return instance

class CustomUserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'total_area', 'cost_per_day', 'area_per_room', 'description']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.user = user

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.company = self.user.company
        if commit:
            instance.save()
        return instance