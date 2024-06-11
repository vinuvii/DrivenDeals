from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from vehicles.models import Vehicle
from user.models import UserProfile

class Bid(models.Model):
    car = models.ForeignKey(Vehicle, related_name='bids', on_delete=models.CASCADE)
    bidder = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bid_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

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