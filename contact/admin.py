from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_details = (
        'email_address',
        'message',
    )


admin.site.register(Contact, ContactAdmin)
