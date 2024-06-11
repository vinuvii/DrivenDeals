from django.db import models
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField(default='')
    mobile_number = models.CharField(max_length=15, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)


