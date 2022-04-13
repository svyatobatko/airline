from django.db import models
from django.core.validators import MinValueValidator
# from django.contrib.gis.db.models import PointField


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
    class Meta:
        db_table = 'aircrafts_data'

    aircraft_code = models.CharField(max_length=3, primary_key=True, null=False)
    model = models.JSONField(null=False)
    range = models.IntegerField(validators=[MinValueValidator(1)], null=False)

    def __str__(self):
        return self.aircraft_code


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
    class Meta:
        db_table = 'airports_data'

    airport_code = models.CharField(max_length=3, primary_key=True, null=False)
    airport_name = models.JSONField(null=False)
    city = models.JSONField(null=False)
#    coordinates = models.PointField(null=False)
    timezone = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.airport_code
