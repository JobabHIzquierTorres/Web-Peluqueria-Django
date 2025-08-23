from django.contrib import admin
from .models import Hours, Info

# Register your models here.


@admin.register(Info)
class AdminInfo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('title', 'description')


@admin.register(Hours)
class AdminHours(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('day', 'get_open', 'get_close', 'is_open', 'order')
    ordering = ['order']

    def get_open(self, obj):
        if not obj.is_open or not obj.open:
            return 'Cerrado'
        return obj.open.strftime('%H:%M')

    def get_close(self, obj):
        if not obj.is_open or not obj.close:
            return 'Cerrado'
        return obj.close.strftime('%H:%M')

    get_open.short_description = 'Hora de apertura'
    get_close.short_description = 'Hora de cierre'
