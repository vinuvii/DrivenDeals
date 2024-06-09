from django.db import models

class Vehicle(models.Model):
    #seller = models.ForeignKey(User, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    picture = models.ImageField(upload_to='vehicle_pictures/', blank=True, null=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.model
