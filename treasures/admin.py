from django.contrib import admin
from .models import Treasure, Category, Image


class TreasureAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'category',
        'description',
        'price',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'display_name',
    )


class ImageAdmin(admin.ModelAdmin):
    list_display = (
        'treasure',
        'image',
    )


admin.site.register(Treasure, TreasureAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Image, ImageAdmin)
