from django.db import models
import pytz
from django.utils import timezone
from django.conf import settings

class Vehicle(models.Model):
    MANUFACTURER_CHOICES = [
        ('Audi', 'Audi'),
        ('BMW', 'BMW'),
        ('Chevrolet', 'Chevrolet'),
        ('Ferrari', 'Ferrari'),
        ('Ford', 'Ford'),
        ('Honda', 'Honda'),
        ('Hyundai', 'Hyundai'),
        ('Jaguar', 'Jaguar'),
        ('Kia', 'Kia'),
        ('Lamborghini', 'Lamborghini'),
        ('Mahindra', 'Mahindra'),
        ('Mazda', 'Mazda'),
        ('McLaren', 'McLaren'),
        ('Mercedes-Benz', 'Mercedes-Benz'),
        ('Mitsubishi', 'Mitsubishi'),
        ('Nissan', 'Nissan'),
        ('Peugeot', 'Peugeot'),
        ('Perodua', 'Perodua'),
        ('Porsche', 'Porsche'),
        ('Renault', 'Renault'),
        ('Rolls-Royce', 'Rolls-Royce'),
        ('Suzuki', 'Suzuki'),
        ('Tata Motors', 'Tata Motors'),
        ('Tesla', 'Tesla'),
        ('Toyota', 'Toyota'),
        ('Volkswagen', 'Volkswagen'),
        ('Volvo', 'Volvo'),
        ('other', 'Other'),
    ]

    BODYTYPE_CHOICES = [
        ('motorbike', 'Motorbike'),
        ('car', 'Car'),
        ('three_wheeler', 'Three Wheeler'),
        ('bicycle', 'Bicycle'),
        ('lorry', 'Lorry'),
        ('truck', 'Truck'),
        ('van', 'Van'),
        ('bus', 'Bus'),
        ('coupe', 'Coupe'),
        ('suv', 'SUV (Sport Utility Vehicle)'),
        ('tractor', 'Tractor'),
        ('atv', 'ATV (All-Terrain Vehicle)'),
        ('sedan', 'Sedan'),
        ('limousine', 'Limousine'),
        ('electric_vehicle', 'Electric Vehicle'),
        ('hybrid_vehicle', 'Hybrid Vehicle'),
        ('offroad_vehicle', 'Off-Road Vehicle'),
        ('other', 'Other'),
    ]
    color = models.CharField(max_length=50, null=True)
    mileage = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    make = models.CharField(max_length=100, choices=MANUFACTURER_CHOICES, null=True)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    body_type = models.CharField(max_length=100, choices=BODYTYPE_CHOICES, null=True)
    no_of_seats = models.PositiveIntegerField(default=0)
    transmission_type = models.CharField(max_length=10, choices=[('Automatic', 'Automatic'), ('Manual', 'Manual')], null=True)
    fuel_type = models.CharField(max_length=20,
                                 choices=[('petrol', 'Petrol'), ('diesel', 'Diesel'), ('electric', 'Electric'),
                                          ('hybrid', 'Hybrid')], null=True)
    engine_capacity = models.DecimalField(max_digits=4, decimal_places=1, null=True)
    engine_type = models.CharField(max_length=32, choices=[('Electric', 'Electric'), ('Hybrid', 'Hybrid'), ('Internal Combustion Engine', 'ICE (Internal Combustion Engine)')], null=True)

    # Additional features
    abs_breaks = models.BooleanField(default=False)
    alloy_wheels = models.BooleanField(default=False)
    airbags = models.BooleanField(default=False)
    air_conditioning = models.BooleanField(default=False)
    power_steering = models.BooleanField(default=False)
    power_windows = models.BooleanField(default=False)
    central_locking = models.BooleanField(default=False)
    reverse_camera = models.BooleanField(default=False)
    sunroof = models.BooleanField(default=False)
    leather_seats = models.BooleanField(default=False)

    picture = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True)
    picture2 = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True)
    picture3 = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True)

    description = models.TextField(blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)

    seller = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True,  null=True)
    auction_duration_days = models.PositiveIntegerField(default=7)
    first_bid_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id and self.posted_date is None:
            asia_kolkata_timezone = pytz.timezone('Asia/Kolkata')
            self.posted_date = timezone.now().astimezone(asia_kolkata_timezone)
        super().save(*args, **kwargs)

    def end_auction(self):
        if self.first_bid_date:
            end_date = self.first_bid_date + timezone.timedelta(days=self.auction_duration_days)
            return timezone.now() > end_date
        return False

    @property
    def auction_ended(self):
        return self.end_auction()

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.timestamp}"
