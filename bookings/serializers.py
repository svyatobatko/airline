from .models import *
from rest_framework import serializers


class AircraftDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AircraftData
        fields = ['aircraft_code', 'model', 'range']


class AirportDataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AirportData
        fields = ['airport_code', 'airport_name', 'city', 'coordinates', 'timezone']


class BoardingPassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BoardingPass
        fields = ['ticket_no', 'flight_id', 'boarding_no', 'seat_no']


class BookingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Booking
        fields = ['book_ref', 'book_date', 'total_amount']


class FlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Flight
        fields = ['flight_id', 'flight_no', 'scheduled_departure', 'scheduled_arrival', 'departure_airport',
                  'arrival_airport', 'status', 'aircraft_code', 'actual_departure', 'actual_arrival']


class SeatSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Seat
        fields = ['aircraft_code', 'seat_no', 'fare_conditions']


class TicketFlightSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TicketFlight
        fields = ['ticket_no', 'flight_id', 'fare_conditions', 'amount']


class TicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ticket
        fields = ['ticket_no', 'book_ref', 'passenger_id', 'passenger_name', 'contact_data']
