from django import forms
from .models import Booking, Rental, Room, Company
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

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

class CustomUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')

    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'description', 'address', 'contact_email']

    def __init__(self, *args, **kwargs):
        user = kwargs.get('user')
        super().__init__(*args, **kwargs)
        if user:
            self.instance.owner = user

    def save(self, *args, **kwargs):
        instance = super().save(commit=False)
        if not instance.owner:
            instance.owner = kwargs.get('user')
        instance.save()
        return instance
