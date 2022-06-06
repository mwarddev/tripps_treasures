from django.contrib import admin
from .models import Shipping


class ShippingAdmin(admin.ModelAdmin):
    list_details = (
        'courier_name',
        'courier_description',
        'delivery_cost',
    )


admin.site.register(Shipping, ShippingAdmin)
