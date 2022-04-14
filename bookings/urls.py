from django.urls import path
from . import views

app_name = "bookings"

urlpatterns = [
    path("", views.HomePage.as_view(), name="index"),
    path("aircrafts/", views.AircraftPage.as_view(), name="aircrafts"),
    path("airports/", views.AirportPage.as_view(), name="airports"),
    path("boarding_passes/", views.BoardingPassPage.as_view(), name="boarding_passes"),
    path("bookings/", views.BoardingPassPage.as_view(), name="bookings"),
    path("flights/", views.FlightPage.as_view(), name="flights"),
    path("seats/", views.SeatPage.as_view(), name="seats"),
    path("ticket_flights/", views.TicketFlightPage.as_view(), name="ticket_flights"),
    path("tickets/", views.TicketPage.as_view(), name="tickets"),
]
