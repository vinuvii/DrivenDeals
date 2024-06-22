# payments/models.py
from django.db import models
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from django.conf import settings


class Payment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20,
                              choices=[('PENDING', 'Pending'), ('COMPLETED', 'Completed'), ('FAILED', 'Failed')])

    def __str__(self):
        return f"Payment of {self.amount} by {self.user.username} for vehicle {self.vehicle.id if self.vehicle else 'N/A'}"
