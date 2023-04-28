from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

import paho.mqtt.client as mqtt
from .mqtt import *

def home(req):
    return render(req, "index.html")

def api(req):
    data = {
        "temperature": serialize("json", list(reversed(Temperature.objects.all()))),
    }
    return JsonResponse(data)

client = mqtt.Client("prauas")
client.message_callback_add('prauas/p1/temperature', on_message_temperature)
client.message_callback_add('prauas/p1/conductivity', on_message_conductivity)
client.message_callback_add('prauas/p1/flow', on_message_flow)
client.message_callback_add('prauas/p1/co', on_message_co)
client.message_callback_add('prauas/p1/amonia', on_message_amonia)
client.message_callback_add('prauas/p1/pressure', on_message_pressure)
client.message_callback_add('prauas/p1/o2', on_message_o2)
client.message_callback_add('prauas/p1/co2', on_message_co2)
client.message_callback_add('prauas/p1/waterlevel', on_message_waterlevel)
client.message_callback_add('prauas/p2/moisture', on_message_moisture)
client.message_callback_add('prauas/p2/ph', on_message_ph)
client.message_callback_add('prauas/p2/sunlight', on_message_sunlight)
client.message_callback_add('prauas/p2/humidity', on_message_humidity)
client.message_callback_add('prauas/p2/anemometer', on_message_anemometer)
client.message_callback_add('prauas/p2/uv', on_message_uv)
client.message_callback_add('prauas/p2/radiation', on_message_radiation)
client.message_callback_add('prauas/p2/berat', on_message_berat)
client.message_callback_add('prauas/p2/color', on_message_color)
client.message_callback_add('prauas/p3/barometer', on_message_barometer)
client.message_callback_add('prauas/p3/wind', on_message_wind)
client.message_callback_add('prauas/p3/visibility', on_message_visibility)
client.message_callback_add('prauas/p3/stock', on_message_stock)
client.message_callback_add('prauas/p3/sellingrate', on_message_sellingrate)
client.message_callback_add('prauas/p3/satisfaction', on_message_satisfaction)
client.message_callback_add('prauas/p3/occupancy', on_message_occupancy)
client.message_callback_add('prauas/p3/audio', on_message_audio)
client.message_callback_add('prauas/p3/sentimen', on_message_sentimen)

client.connect('localhost', 1883)
client.loop_start()
client.subscribe('prauas/#')