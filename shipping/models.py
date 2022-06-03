from django.db import models


class Shipping(models.Model):
    """
    Model for multiple shipping options with scope for
    the site owner to update prices and add/remove couriers
    """
    courier_name = models.CharField(max_length=50, null=False, blank=False)
    courier_descripton = models.TextField()
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)

    def __str__(self):
        return f'Courier: {self.courier_name} £{self.delivery_cost}'
