from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import PurchaseItem


@receiver(post_save, sender=PurchaseItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update the purchase total for PurchaseItems on creation or update
    """
    instance.purchase.calc_total()


@receiver(post_delete, sender=PurchaseItem)
def update_on_delete(sender, instance, **kwargs):
    """
    Update purchase total on PurchaseItem delete
    """
    instance.purchase.calc_total()
