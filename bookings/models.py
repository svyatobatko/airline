from django.db import models
from django.core.validators import MinValueValidator
from viewflow.fields import CompositeKey


CONDITION = (
    ('Economy', 'Economy'),
    ('Comfort', 'Comfort'),
    ('Business', 'Business'),
)


#     Столбец    |   Тип   | Модификаторы |             Описание
# ---------------+---------+--------------+-----------------------------------
#  aircraft_code | char(3) | not null     | Код самолета, IATA
#  model         | text    | not null     | Модель самолета                      в БД JSON
#  range         | integer | not null     | Максимальная дальность полета, км
# Индексы: PRIMARY KEY, btree(aircraft_code)
# Ограничения - проверки: CHECK(range > 0)
# Ссылки извне:
#    TABLE "flights" FOREIGN KEY (aircraft_code) REFERENCES aircrafts_data(aircraft_code)
#    TABLE "seats" FOREIGN KEY (aircraft_code) REFERENCES aircrafts_data(aircraft_code) ON DELETE CASCADE
class AircraftData(models.Model):
    aircraft_code = models.CharField(max_length=3, primary_key=True, null=False, unique=True)
    model = models.JSONField(null=False)
    range = models.IntegerField(validators=[MinValueValidator(1)], null=False)

    class Meta:
        db_table = 'aircrafts_data'

    def display_model(self):
        return '%s' % self.model['en']


#    Столбец    |   Тип   | Модификаторы |                 Описание
# --------------+---------+--------------+--------------------------------------------
#  airport_code | char(3) | not null     | Код аэропорта
#  airport_name | jsonb   | not null     | Название аэропорта
#  city         | jsonb   | not null     | Город
#  coordinates  | point   | not null     | Координаты аэропорта (долгота и широта)
#  timezone     | text    | not null     | Часовой пояс аэропорта
# Индексы: PRIMARY KEY, btree (airport_code)
# Ссылки извне:
#     TABLE "flights" FOREIGN KEY (arrival_airport) REFERENCES airports_data(airport_code)
#     TABLE "flights" FOREIGN KEY (departure_airport) REFERENCES airports_data(airport_code)
class AirportData(models.Model):
    airport_code = models.CharField(max_length=3, primary_key=True, null=False, unique=True)
    airport_name = models.JSONField(null=False)
    city = models.JSONField(null=False)
    # can be make as PointField
    coordinates = models.Field(null=False)
    timezone = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = 'airports_data'

    def display_airport_name(self):
        return '%s' % self.airport_name['en']

    def display_city(self):
        return '%s' % self.city['en']


#    Столбец   |    Тип     | Модификаторы |         Описание
# -------------+------------+--------------+--------------------------
#  ticket_no   | char(13)   | not null     | Номер билета
#  flight_id   | integer    | not null     | Идентификатор рейса
#  boarding_no | integer    | not null     | Номер посадочного талона
#  seat_no     | varchar(4) | not null     | Номер места
# Индексы:
#    PRIMARY KEY, btree (ticket_no, flight_id)
#    UNIQUE CONSTRAINT, btree (flight_id, boarding_no)
#    UNIQUE CONSTRAINT, btree (flight_id, seat_no)
# Ограничения внешнего ключа: FOREIGN KEY (ticket_no, flight_id) REFERENCES ticket_flights(ticket_no, flight_id)
class BoardingPass(models.Model):
    id = CompositeKey(columns=['ticket_no', 'flight_id'])
    ticket_no = models.CharField(max_length=13, primary_key=True, null=False)
    flight_id = models.IntegerField(null=False)
    boarding_no = models.IntegerField(null=False)
    seat_no = models.CharField(max_length=4, null=False)

    class Meta:
        db_table = 'boarding_passes'
        unique_together = (('ticket_no', 'flight_id'),)


#    Столбец    |      Тип      | Модификаторы |         Описание
# --------------+---------------+--------------+---------------------------
#  book_ref     | char(6)       | not null     | Номер бронирования
#  book_date    | timestamptz   | not null     | Дата бронирования
#  total_amount | numeric(10,2) | not null     | Полная сумма бронирования
# Индексы: PRIMARY KEY, btree (book_ref)
# Ссылки извне: TABLE "tickets" FOREIGN KEY (book_ref) REFERENCES bookings(book_ref)
class Booking(models.Model):
    book_ref = models.CharField(max_length=6, primary_key=True, null=False, unique=True)
    book_date = models.DateTimeField(null=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = 'bookings'


#        Столбец       |     Тип     | Модификаторы |          Описание
# ---------------------+-------------+--------------+-----------------------------
#  flight_id           | serial      | not null     | Идентификатор рейса
#  flight_no           | char(6)     | not null     | Номер рейса
#  scheduled_departure | timestamptz | not null     | Время вылета по расписанию
#  scheduled_arrival   | timestamptz | not null     | Время прилёта по расписанию
#  departure_airport   | char(3)     | not null     | Аэропорт отправления
#  arrival_airport     | char(3)     | not null     | Аэропорт прибытия
#  status              | varchar(20) | not null     | Статус рейса
#  aircraft_code       | char(3)     | not null     | Код самолета, IATA
#  actual_departure    | timestamptz |              | Фактическое время вылета
#  actual_arrival      | timestamptz |              | Фактическое время прилёта
# Индексы: PRIMARY KEY, btree (flight_id)
#    UNIQUE CONSTRAINT, btree (flight_no, scheduled_departure)
# Ограничения-проверки:
#    CHECK (scheduled_arrival > scheduled_departure)
#    CHECK ((actual_arrival IS NULL)
#       OR  ((actual_departure IS NOT NULL AND actual_arrival IS NOT NULL)
#            AND (actual_arrival > actual_departure)))
#    CHECK (status IN ('On Time', 'Delayed', 'Departed','Arrived', 'Scheduled', 'Cancelled'))
# Ограничения внешнего ключа:
#     FOREIGN KEY (aircraft_code) REFERENCES aircrafts(aircraft_code)
#     FOREIGN KEY (arrival_airport) REFERENCES airports(airport_code)
#     FOREIGN KEY (departure_airport) REFERENCES airports(airport_code)
# Ссылки извне: TABLE "ticket_flights" FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
class Flight(models.Model):
    flight_id = models.IntegerField(unique=True, primary_key=True, null=False)
    flight_no = models.CharField(max_length=6, null=False)
    scheduled_departure = models.DateTimeField(null=False)
    scheduled_arrival = models.DateTimeField(null=False)
    departure_airport = models.ForeignKey(AirportData, db_column='departure_airport', related_name='departure_airport',
                                          on_delete=models.NOT_PROVIDED, null=False)
    arrival_airport = models.ForeignKey(AirportData, db_column='arrival_airport', related_name='arrival_airport',
                                        on_delete=models.NOT_PROVIDED, null=False)
    status = models.CharField(max_length=20, null=False)
    aircraft_code = models.ForeignKey(AircraftData, db_column='aircraft_code',
                                      on_delete=models.NOT_PROVIDED, null=False)
    actual_departure = models.DateTimeField()
    actual_arrival = models.DateTimeField()

    class Meta:
        db_table = 'flights'


#      Столбец     |     Тип     | Модификаторы |      Описание
# -----------------+-------------+--------------+--------------------
#  aircraft_code   | char(3)     | not null     | Код самолета, IATA
#  seat_no         | varchar(4)  | not null     | Номер места
#  fare_conditions | varchar(10) | not null     | Класс обслуживания
# Индексы: PRIMARY KEY, btree (aircraft_code, seat_no)
# Ограничения-проверки: CHECK (fare_conditions IN ('Economy', 'Comfort', 'Business'))
# Ограничения внешнего ключа: FOREIGN KEY (aircraft_code)  REFERENCES aircrafts(aircraft_code) ON DELETE CASCADE
class Seat(models.Model):
    id = CompositeKey(columns=['aircraft_code', 'seat_no'])
    aircraft_code = models.ForeignKey(AircraftData, db_column='aircraft_code', on_delete=models.CASCADE,
                                      null=False)
    seat_no = models.CharField(max_length=4, primary_key=True, null=False)
    fare_conditions = models.CharField(max_length=20, choices=CONDITION, null=False)

    class Meta:
        db_table = 'seats'
        unique_together = (('aircraft_code', 'seat_no'),)


#      Столбец     |     Тип       | Модификаторы |    Описание
# -----------------+---------------+--------------+---------------------
#  ticket_no       | char(13)      | not null     | Номер билета
#  flight_id       | integer       | not null     | Идентификатор рейса
#  fare_conditions | varchar(10)   | not null     | Класс обслуживания
#  amount          | numeric(10,2) | not null     | Стоимость перелета
# Индексы: PRIMARY KEY, btree (ticket_no, flight_id)
# Ограничения-проверки:   CHECK (amount >= 0)
#                         CHECK (fare_conditions IN ('Economy', 'Comfort', 'Business'))
# Ограничения внешнего ключа: FOREIGN KEY (flight_id) REFERENCES flights(flight_id)
#                             FOREIGN KEY (ticket_no) REFERENCES tickets(ticket_no)
# Ссылки извне: TABLE "boarding_passes" FOREIGN KEY (ticket_no, flight_id)
#                       REFERENCES ticket_flights(ticket_no, flight_id)
class TicketFlight(models.Model):
    id = CompositeKey(columns=['ticket_no', 'flight_id'])
    ticket_no = models.CharField(max_length=13, primary_key=True, null=False)
    flight_id = models.IntegerField(null=False)
    fare_conditions = models.CharField(max_length=10, choices=CONDITION, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    class Meta:
        db_table = 'ticket_flights'
        unique_together = (('ticket_no', 'flight_id'),)


#      Столбец    |     Тип     | Модификаторы |          Описание
# ----------------+-------------+--------------+-----------------------------
#  ticket_no      | char(13)    | not null     | Номер билета
#  book_ref       | char(6)     | not null     | Номер бронирования
#  passenger_id   | varchar(20) | not null     | Идентификатор пассажира
#  passenger_name | text        | not null     | Имя пассажира
#  contact_data   | jsonb       |              | Контактные данные пассажира
# Индексы: PRIMARY KEY, btree (ticket_no)
# Ограничения внешнего ключа: FOREIGN KEY (book_ref) REFERENCES bookings(book_ref)
# Ссылки извне: TABLE "ticket_flights" FOREIGN KEY (ticket_no) REFERENCES tickets(ticket_no)
class Ticket(models.Model):
    ticket_no = models.CharField(max_length=13, primary_key=True, null=False)
    book_ref = models.ForeignKey(Booking, db_column='book_ref', on_delete=models.NOT_PROVIDED, null=False)
    passenger_id = models.CharField(max_length=20, null=False)
    passenger_name = models.TextField(null=False)
    contact_data = models.JSONField(null=False)

    class Meta:
        db_table = 'tickets'
