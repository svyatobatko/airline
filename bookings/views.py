from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, permissions, filters

from .models import *
from .serializers import *


class AircraftViewSet(generics.ListAPIView):
    queryset = AircraftData.objects.all()
    serializer_class = AircraftDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['aircraft_code', 'range']
    ordering_fields = ['aircraft_code', 'range']


class AirportViewSet(generics.ListAPIView):
    queryset = AirportData.objects.all()
    serializer_class = AirportDataSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['airport_code', 'coordinates', 'timezone']
    ordering_fields = ['airport_code', 'coordinates', 'timezone']


class BoardingViewSet(generics.ListAPIView):
    queryset = BoardingPass.objects.all()
    serializer_class = BoardingPassSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ticket_no', 'flight_id', 'boarding_no', 'seat_no']
    ordering_fields = ['ticket_no', 'flight_id', 'boarding_no', 'seat_no']


class BookingViewSet(generics.ListAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['book_ref', 'book_date', 'total_amount']
    ordering_fields = ['book_ref', 'book_date', 'total_amount']


class FlightViewSet(generics.ListAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                        'arrival_airport', 'status', 'aircraft_code', 'actual_departure', 'actual_arrival']
    ordering_fields = ['flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                       'arrival_airport', 'status', 'aircraft_code', 'actual_departure', 'actual_arrival']


class SeatViewSet(generics.ListAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['aircraft_code', 'seat_no', 'fare_conditions']
    ordering_fields = ['aircraft_code', 'seat_no', 'fare_conditions']


class TicketFlightViewSet(generics.ListAPIView):
    queryset = TicketFlight.objects.all()
    serializer_class = TicketFlightSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ticket_no', 'flight_id', 'fare_conditions', 'amount']
    ordering_fields = ['ticket_no', 'flight_id', 'fare_conditions', 'amount']


class TicketViewSet(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['ticket_no', 'book_ref', 'passenger_id', 'passenger_name']
    ordering_fields = ['ticket_no', 'book_ref', 'passenger_id', 'passenger_name']
