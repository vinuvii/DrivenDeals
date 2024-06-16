from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from django.conf import settings

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    BID_STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('ACCEPTED', 'Accepted'),
        ('REJECTED', 'Rejected'),
        ('EXPIRED', 'Expired'),
    ]
    bid_status = models.CharField(max_length=10, choices=BID_STATUS_CHOICES, default='PENDING')

    expiry_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id and self.car:
            self.expiry_date = self.car.posted_date + timezone.timedelta(weeks=1)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Bid for {self.car} by {self.bidder}"