from django.contrib import admin
from .models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = (
        'info',
    )


admin.site.register(Banner, BannerAdmin)
