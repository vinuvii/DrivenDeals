from django.db import models
from django.utils import timezone
from vehicles.models import Vehicle
from django.conf import settings

class Bid(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    BID_STATUS_PENDING = 'PENDING'
    BID_STATUS_ACCEPTED = 'ACCEPTED'
    BID_STATUS_REJECTED = 'REJECTED'
    BID_STATUS_EXPIRED = 'EXPIRED'

    BID_STATUS_CHOICES = [
        (BID_STATUS_PENDING, 'Pending'),
        (BID_STATUS_ACCEPTED, 'Accepted'),
        (BID_STATUS_REJECTED, 'Rejected'),
        (BID_STATUS_EXPIRED, 'Expired'),
    ]
    bid_status = models.CharField(max_length=10, choices=BID_STATUS_CHOICES, default=BID_STATUS_PENDING)

    expiry_date = models.DateTimeField()

    def save(self, *args, **kwargs):
        if not self.id:
            if self.vehicle:
                if not self.expiry_date:
                    if self.vehicle.first_bid_date:
                        self.expiry_date = self.vehicle.first_bid_date + timezone.timedelta(days=self.vehicle.auction_duration_days)
                    else:
                        # Handle case where first_bid_date is None (no bids yet)
                        self.expiry_date = timezone.now() + timezone.timedelta(days=self.vehicle.auction_duration_days)
        super().save(*args, **kwargs)

    def update_bid_status(self):
        # Check if the bid is expired
        if self.expiry_date and self.expiry_date <= timezone.now():
            # Only update status if it's still pending
            if self.bid_status == self.BID_STATUS_PENDING:
                highest_bid = Bid.objects.filter(vehicle=self.vehicle, bid_status=self.BID_STATUS_PENDING).exclude(id=self.id).order_by('-amount').first()
                if highest_bid and highest_bid.amount > self.amount:
                    self.bid_status = self.BID_STATUS_REJECTED
                else:
                    self.bid_status = self.BID_STATUS_ACCEPTED if highest_bid else self.BID_STATUS_EXPIRED
                self.save()

    def __str__(self):
        return f"Bid for {self.vehicle} by {self.user}"

    class Meta:
        ordering = ['-amount']