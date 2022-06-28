from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django_countries.fields import CountryField


class UserAccount(models.Model):
    """
    A user account model for storing delivery
    information and purchase history
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    saved_full_name = models.CharField(max_length=100, null=True, blank=True)
    saved_phone = models.CharField(max_length=20, null=True, blank=True)
    saved_address_line1 = models.CharField(max_length=100,
                                           null=True,
                                           blank=True)
    saved_address_line2 = models.CharField(max_length=100,
                                           null=True,
                                           blank=True)
    saved_city = models.CharField(max_length=50, null=True, blank=True)
    saved_county = models.CharField(max_length=100, null=True, blank=True)
    saved_country = CountryField(blank_label='Country *',
                                 null=True,
                                 blank=True)
    saved_postcode = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_or_update_user_account(sender, instance, created, **kwargs):
    """
    Create or update the user profile
    """
    if created:
        UserAccount.objects.create(user=instance)
    # Existing users: just save the account
    instance.useraccount.save()
