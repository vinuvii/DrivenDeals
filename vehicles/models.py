from django.db import models
import pytz
from django.utils import timezone

class Vehicle(models.Model):
    #seller = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True)
    description = models.TextField(blank=True)
    posted_date = models.DateTimeField(null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id and self.posted_date is None:
            asia_kolkata_timezone = pytz.timezone('Asia/Kolkata')
            self.posted_date = timezone.now().astimezone(asia_kolkata_timezone)
            super().save(*args, **kwargs)
        else:
            if self.posted_date:
                asia_kolkata_timezone = pytz.timezone('Asia/Kolkata')
                utc_posted_date = self.posted_date.astimezone(pytz.utc)
                self.posted_date = utc_posted_date.astimezone(asia_kolkata_timezone)

            self.__class__.objects.filter(pk=self.pk).update(posted_date=self.posted_date)

    def __str__(self):
        return self.model
