from rest_framework.response import Response
from .models import *

def on_message_temperature(client, userdata, msg):
    Temperature.objects.create(value=msg.payload.decode("utf-8"))
    if Temperature.objects.count() > 200:
        Temperature.objects.all().first().delete()

def on_message_conductivity(client, userdata, msg):
    Conductivity.objects.create(value=msg.payload.decode("utf-8"))
    if Conductivity.objects.count() > 200:
        Conductivity.objects.all().first().delete()

def on_message_flow(client, userdata, msg):
    Flow.objects.create(value=msg.payload.decode("utf-8"))
    if Flow.objects.count() > 200:
        Flow.objects.all().first().delete()

def on_message_co(client, userdata, msg):
    CO.objects.create(value=msg.payload.decode("utf-8"))
    if CO.objects.count() > 200:
        CO.objects.all().first().delete()

def on_message_amonia(client, userdata, msg):
    Amonia.objects.create(value=msg.payload.decode("utf-8"))
    if Amonia.objects.count() > 200:
        Amonia.objects.all().first().delete()

def on_message_pressure(client, userdata, msg):
    Pressure.objects.create(value=msg.payload.decode("utf-8"))
    if Pressure.objects.count() > 200:
        Pressure.objects.all().first().delete()

def on_message_o2(client, userdata, msg):
    O2.objects.create(value=msg.payload.decode("utf-8"))
    if O2.objects.count() > 200:
        O2.objects.all().first().delete()

def on_message_co2(client, userdata, msg):
    CO2.objects.create(value=msg.payload.decode("utf-8"))
    if CO2.objects.count() > 200:
        CO2.objects.all().first().delete()

def on_message_waterlevel(client, userdata, msg):
    Waterlevel.objects.create(value=msg.payload.decode("utf-8"))
    if Waterlevel.objects.count() > 200:
        Waterlevel.objects.all().first().delete()

def on_message_moisture(client, userdata, msg):
    Moisture.objects.create(value=msg.payload.decode("utf-8"))
    if Moisture.objects.count() > 200:
        Moisture.objects.all().first().delete()

def on_message_ph(client, userdata, msg):
    PH.objects.create(value=msg.payload.decode("utf-8"))
    if PH.objects.count() > 200:
        PH.objects.all().first().delete()

def on_message_sunlight(client, userdata, msg):
    Sunlight.objects.create(value=msg.payload.decode("utf-8"))
    if Sunlight.objects.count() > 200:
        Sunlight.objects.all().first().delete()

def on_message_humidity(client, userdata, msg):
    Humidity.objects.create(value=msg.payload.decode("utf-8"))
    if Humidity.objects.count() > 200:
        Humidity.objects.all().first().delete()

def on_message_anemometer(client, userdata, msg):
    Anemometer.objects.create(value=msg.payload.decode("utf-8"))
    if Anemometer.objects.count() > 200:
        Anemometer.objects.all().first().delete()

def on_message_uv(client, userdata, msg):
    UV.objects.create(value=msg.payload.decode("utf-8"))
    if UV.objects.count() > 200:
        UV.objects.all().first().delete()

def on_message_radiation(client, userdata, msg):
    Radiation.objects.create(value=msg.payload.decode("utf-8"))
    if Radiation.objects.count() > 200:
        Radiation.objects.all().first().delete()

def on_message_berat(client, userdata, msg):
    Berat.objects.create(value=msg.payload.decode("utf-8"))
    if Berat.objects.count() > 200:
        Berat.objects.all().first().delete()

def on_message_color(client, userdata, msg):
    Color.objects.create(value=msg.payload.decode("utf-8"))
    if Color.objects.count() > 200:
        Color.objects.all().first().delete()

def on_message_barometer(client, userdata, msg):
    Barometer.objects.create(value=msg.payload.decode("utf-8"))
    if Barometer.objects.count() > 200:
        Barometer.objects.all().first().delete()

def on_message_wind(client, userdata, msg):
    Wind.objects.create(value=msg.payload.decode("utf-8"))
    if Wind.objects.count() > 200:
        Wind.objects.all().first().delete()

def on_message_visibility(client, userdata, msg):
    Visibility.objects.create(value=msg.payload.decode("utf-8"))
    if Visibility.objects.count() > 200:
        Visibility.objects.all().first().delete()

def on_message_stock(client, userdata, msg):
    Stock.objects.create(value=msg.payload.decode("utf-8"))
    if Stock.objects.count() > 200:
        Stock.objects.all().first().delete()

def on_message_sellingrate(client, userdata, msg):
    Sellingrate.objects.create(value=msg.payload.decode("utf-8"))
    if Sellingrate.objects.count() > 200:
        Sellingrate.objects.all().first().delete()

def on_message_satisfaction(client, userdata, msg):
    Satisfaction.objects.create(value=msg.payload.decode("utf-8"))
    if Satisfaction.objects.count() > 200:
        Satisfaction.objects.all().first().delete()

def on_message_occupancy(client, userdata, msg):
    Occupancy.objects.create(value=msg.payload.decode("utf-8"))
    if Occupancy.objects.count() > 200:
        Occupancy.objects.all().first().delete()

def on_message_audio(client, userdata, msg):
    Audio.objects.create(value=msg.payload.decode("utf-8"))
    if Audio.objects.count() > 200:
        Audio.objects.all().first().delete()

def on_message_sentimen(client, userdata, msg):
    Sentimen.objects.create(value=msg.payload.decode("utf-8"))
    if Sentimen.objects.count() > 200:
        Sentimen.objects.all().first().delete()
