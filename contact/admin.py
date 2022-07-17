from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_details = (
        'cust_name',
        'email_address',
        'message',
        'message_date',
        'purchase_number',
    )


admin.site.register(Contact, ContactAdmin)
