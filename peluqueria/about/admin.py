from django.contrib import admin
from .models import About, Barbers

# Register your models here.


class AboutAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(About, AboutAdmin)


@admin.register(Barbers)
class BarbersAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
