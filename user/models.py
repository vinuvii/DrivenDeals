from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver



class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_address = models.EmailField(default='')
    mobile_number = models.CharField(max_length=15, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)
    trading_address = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()


class Listing(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def get_absolute_url(self):
        return reverse('listing_detail', kwargs={'pk': self.pk})

class WatchlistItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_id = models.IntegerField()  # Assuming item_id is an integer field representing the ID of the watched item

    class Meta:
        unique_together = ('user', 'item_id')