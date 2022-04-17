from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path("aircrafts/", views.AircraftViewSet.as_view(), name="aircrafts"),
    path("airports/", views.AirportViewSet.as_view(), name="airports"),
    path("boarding_passes/", views.BoardingViewSet.as_view(), name="boarding_passes"),
    path("bookings/", views.BookingViewSet.as_view(), name="bookings"),
    path("flights/", views.FlightViewSet.as_view(), name="flights"),
    path("seats/", views.SeatViewSet.as_view(), name="seats"),
    path("ticket_flights/", views.TicketFlightViewSet.as_view(), name="ticket_flights"),
    path("tickets/", views.TicketViewSet.as_view(), name="tickets"),
]
