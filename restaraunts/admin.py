
from django.contrib import admin
from .models import Restaraunt, Category

# Register your models here.


class RestarauntAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'image_url',
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Restaraunt, RestarauntAdmin)
admin.site.register(Category, CategoryAdmin)