from django.contrib import admin

from products.models import


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['phone_number', 'price', 'is_new', ]

