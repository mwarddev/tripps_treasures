from django.contrib import admin
from .models import Purchase, PurchaseItem


class PurchaseItemAdminInline(admin.TabularInline):
    model = PurchaseItem
    readonly_fields = ('item_total',)


class PurchaseAdmin(admin.ModelAdmin):
    inlines = (PurchaseItemAdminInline,)

    readonly_fields = ('purchase_number', 'purchase_date',
                       'subtotal', 'grand_total',
                       'original_basket', 'stripe_pid',)

    fields = ('purchase_number', 'user_account',
              'full_name', 'email', 'phone', 'address_line1',
              'address_line2', 'city', 'county', 'country',
              'postcode', 'purchase_date', 'shipping',
              'subtotal','grand_total', 'original_basket',
              'stripe_pid','purchase_status')

    list_display = ('purchase_number', 'purchase_date',
                    'full_name','subtotal','shipping',
                    'grand_total')

    ordering = ('-purchase_date',)


admin.site.register(Purchase, PurchaseAdmin)
