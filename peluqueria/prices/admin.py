from django.contrib import admin

from .models import Info, Prices

# Register your models here.


@admin.register(Prices)
class AdminPrices(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('service', 'price')


@admin.register(Info)
class AdminInfo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
