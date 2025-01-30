from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Company(models.Model):
    name = models.CharField(max_length=255)
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.name:
            raise ValidationError("Company name cannot be empty.")
        super().save(*args, **kwargs)


class Room(models.Model):
    name = models.CharField(max_length=255)
    total_area = models.IntegerField(help_text="Total area in square meters")
    cost_per_day = models.DecimalField(max_digits=10, decimal_places=2, help_text="Cost per day for renting the room")
    area_per_room = models.IntegerField(help_text="Area per sub-room in square meters")
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='rooms')
    number_of_rooms = models.IntegerField(help_text="Number of rooms in the premises", default=1)

    def __str__(self):
        return self.name

    def clean(self):
        if self.cost_per_day <= 0:
            raise ValidationError("Cost per day must be greater than zero.")
        if self.area_per_room <= 0:
            raise ValidationError("Area per room must be greater than zero.")
        if self.total_area <= 0:
            raise ValidationError("Total area must be greater than zero.")
        if self.number_of_rooms <= 0:
            raise ValidationError("Number of rooms must be greater than zero.")


    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room.name} - {self.user.username} ({self.start_date} to {self.end_date})"

    def clean(self):
        if self.end_date <= self.start_date:
            raise ValidationError("End date must be after the start date.")


    def save(self, *args, **kwargs):
        self.clean()
        self.total_cost = (self.end_date - self.start_date).days * self.room.cost_per_day
        super().save(*args, **kwargs)


class Rental(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='rentals')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rental_date = models.DateField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.room.name} - {self.user.username} ({self.rental_date})"

    def clean(self):
        if self.rental_date < models.DateField().today():
            raise ValidationError("Rental date cannot be in the past.")

    def save(self, *args, **kwargs):
        self.clean()
        self.cost = self.room.cost_per_day
        super().save(*args, **kwargs)
