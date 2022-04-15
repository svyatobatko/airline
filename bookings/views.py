from django.views.generic import TemplateView

from .models import *


class HomePage(TemplateView):
    http_method_names = ["get"]
    template_name = "homepage.html"


class AircraftPage(TemplateView):
    http_method_names = ["get"]
    template_name = "aircrafts.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        aircrafts = AircraftData.objects.all().order_by('aircraft_code')
        context['aircrafts'] = aircrafts
        return context


class AirportPage(TemplateView):
    http_method_names = ["get"]
    template_name = "airports.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        airports = AirportData.objects.all().order_by('airport_code')
        context['airports'] = airports
        return context


class BoardingPassPage(TemplateView):
    http_method_names = ["get"]
    template_name = "boarding_passes.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        boarding_passes = BoardingPass.objects.all().order_by('id')[0:100]
        context['boarding_passes'] = boarding_passes
        return context


class BookingPage(TemplateView):
    http_method_names = ["get"]
    template_name = "bookings.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        bookings = Booking.objects.all().order_by('book_ref')[0:100]
        context['bookings'] = bookings
        return context


class FlightPage(TemplateView):
    http_method_names = ["get"]
    template_name = "flights.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        flights = Flight.objects.all().order_by('flight_id')[0:100]
        context['flights'] = flights
        return context


class SeatPage(TemplateView):
    http_method_names = ["get"]
    template_name = "seats.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        seats = Seat.objects.all().order_by('id')[0:100]
        context['seats'] = seats
        return context


class TicketFlightPage(TemplateView):
    http_method_names = ["get"]
    template_name = "ticket_flights.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        ticket_flights = TicketFlight.objects.all().order_by('id')[0:100]
        context['ticket_flights'] = ticket_flights
        return context


class TicketPage(TemplateView):
    http_method_names = ["get"]
    template_name = "tickets.html"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        tickets = Ticket.objects.all().order_by('ticket_no')[0:100]
        context['tickets'] = tickets
        return context
