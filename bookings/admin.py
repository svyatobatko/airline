from django.contrib import admin
from .models import *


class AircraftDataAdmin(admin.ModelAdmin):
    list_display = ('aircraft_code', 'display_model', 'range')
    list_filter = ('aircraft_code', 'model', 'range')


class AirportDataAdmin(admin.ModelAdmin):
    list_display = ('airport_code', 'display_airport_name', 'display_city', 'coordinates', 'timezone')
    list_filter = ('airport_code', 'airport_name', 'city', 'timezone')


class BoardingPassAdmin(admin.ModelAdmin):
    list_display = ('ticket_no', 'flight_id', 'boarding_no', 'seat_no')
    list_filter = ('ticket_no', 'flight_id', 'boarding_no', 'seat_no')


class BookingAdmin(admin.ModelAdmin):
    list_display = ('book_ref', 'book_date', 'total_amount')
    list_filter = ('book_ref', 'book_date', 'total_amount')


class FlightAdmin(admin.ModelAdmin):
    list_display = ('flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                    'arrival_airport', 'status', 'aircraft_code', 'actual_departure', 'actual_arrival')
    list_filter = ('flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                   'arrival_airport', 'status', 'aircraft_code', 'actual_departure', 'actual_arrival')


class SeatAdmin(admin.ModelAdmin):
    list_display = ('aircraft_code', 'seat_no', 'fare_conditions')
    list_filter = ('aircraft_code', 'seat_no', 'fare_conditions')


class TicketFlightAdmin(admin.ModelAdmin):
    list_display = ('ticket_no', 'flight_id', 'fare_conditions', 'amount')
    list_filter = ('ticket_no', 'flight_id', 'fare_conditions', 'amount')


class TicketAdmin(admin.ModelAdmin):
    list_display = ('ticket_no', 'book_ref', 'passenger_id', 'passenger_name')
    list_filter = ('ticket_no', 'book_ref', 'passenger_id', 'passenger_name')


admin.site.register(AircraftData, AircraftDataAdmin)
admin.site.register(AirportData, AirportDataAdmin)
admin.site.register(BoardingPass, BoardingPassAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Flight, FlightAdmin)
admin.site.register(Seat, SeatAdmin)
admin.site.register(TicketFlight, TicketFlightAdmin)
admin.site.register(Ticket, TicketAdmin)
