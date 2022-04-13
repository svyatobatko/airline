from django.contrib import admin
from .models import *


class AircraftDataAdmin(admin.ModelAdmin):
    pass


class AirportDataAdmin(admin.ModelAdmin):
    pass


admin.site.register(AircraftData, AircraftDataAdmin)
admin.site.register(AirportData, AirportDataAdmin)
