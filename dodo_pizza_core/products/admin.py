from django.contrib import admin

from products.models import Pizza, Drink


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'is_new', ]

@admin.register(Drink)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'volume']

