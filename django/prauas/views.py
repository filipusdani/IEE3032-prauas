from django.shortcuts import render
from django.http import JsonResponse
from django.core.serializers import serialize

import paho.mqtt.client as mqtt
from .mqtt import *
from .ml import *

def home(req):
    return render(req, "index.html")

def api(req):
    milking_machine,slaughter_machine,feeding_machine,gramasi_karbo,sprayer,pemberi_pupuk,aircon,hasil_penjualan,jumlah_kursi,output_produk,hasil_tanam,proyeksi_keuntungan,nilai_pabrik = hitung_ml()
    data = {
        "Temperature": serialize("json", list(reversed(Temperature.objects.all()))),
        "Conductivity": serialize("json", list(reversed(Conductivity.objects.all()))),
        "Flow": serialize("json", list(reversed(Flow.objects.all()))),
        "CO": serialize("json", list(reversed(CO.objects.all()))),
        "Amonia": serialize("json", list(reversed(Amonia.objects.all()))),
        "Pressure": serialize("json", list(reversed(Pressure.objects.all()))),
        "O2": serialize("json", list(reversed(O2.objects.all()))),
        "CO2": serialize("json", list(reversed(CO2.objects.all()))),
        "Waterlevel": serialize("json", list(reversed(Waterlevel.objects.all()))),
        "Moisture": serialize("json", list(reversed(Moisture.objects.all()))),
        "PH": serialize("json", list(reversed(PH.objects.all()))),
        "Sunlight": serialize("json", list(reversed(Sunlight.objects.all()))),
        "Humidity": serialize("json", list(reversed(Humidity.objects.all()))),
        "Anemometer": serialize("json", list(reversed(Anemometer.objects.all()))),
        "UV": serialize("json", list(reversed(UV.objects.all()))),
        "Radiation": serialize("json", list(reversed(Radiation.objects.all()))),
        "Berat": serialize("json", list(reversed(Berat.objects.all()))),
        "Color": serialize("json", list(reversed(Color.objects.all()))),
        "Barometer": serialize("json", list(reversed(Barometer.objects.all()))),
        "Wind": serialize("json", list(reversed(Wind.objects.all()))),
        "Visibility": serialize("json", list(reversed(Visibility.objects.all()))),
        "Stock": serialize("json", list(reversed(Stock.objects.all()))),
        "Sellingrate": serialize("json", list(reversed(Sellingrate.objects.all()))),
        "Satisfaction": serialize("json", list(reversed(Satisfaction.objects.all()))),
        "Occupancy": serialize("json", list(reversed(Occupancy.objects.all()))),
        "Audio": serialize("json", list(reversed(Audio.objects.all()))),
        "Sentimen": serialize("json", list(reversed(Sentimen.objects.all()))),
        "milking_machine": milking_machine,
        "slaughter_machine": slaughter_machine,
        "feeding_machine": feeding_machine,
        "gramasi_karbo": gramasi_karbo,
        "sprayer": sprayer,
        "pemberi_pupuk": pemberi_pupuk,
        "aircon": aircon,
        "hasil_penjualan": hasil_penjualan,
        "jumlah_kursi": jumlah_kursi,
        "output_produk": output_produk,
        "hasil_tanam": hasil_tanam,
        "proyeksi_keuntungan": proyeksi_keuntungan,
        "nilai_pabrik": nilai_pabrik,
    }
    return JsonResponse(data)

def hitung_ml():
    aTemperature = (list(reversed(Temperature.objects.all())))[0].value
    aConductivity = (list(reversed(Conductivity.objects.all())))[0].value
    aFlow = (list(reversed(Flow.objects.all())))[0].value
    aCO = (list(reversed(CO.objects.all())))[0].value
    aAmonia = (list(reversed(Amonia.objects.all())))[0].value
    aPressure = (list(reversed(Pressure.objects.all())))[0].value
    aO2 = (list(reversed(O2.objects.all())))[0].value
    aCO2 = (list(reversed(CO2.objects.all())))[0].value
    aWaterlevel = (list(reversed(Waterlevel.objects.all())))[0].value
    milking_machine = hitung_milking_machine(aTemperature,aConductivity,aFlow)
    slaughter_machine = hitung_slaughter_machine(aCO,aAmonia,aPressure)
    feeding_machine = hitung_feeding_machine(aO2,aCO2,aWaterlevel)

    aMoisture = (list(reversed(Moisture.objects.all())))[0].value
    aPH = (list(reversed(PH.objects.all())))[0].value
    aSunlight = (list(reversed(Sunlight.objects.all())))[0].value
    aHumidity = (list(reversed(Humidity.objects.all())))[0].value
    aAnemometer = (list(reversed(Anemometer.objects.all())))[0].value
    aUV = (list(reversed(UV.objects.all())))[0].value
    aRadiation = (list(reversed(Radiation.objects.all())))[0].value
    aBerat = (list(reversed(Berat.objects.all())))[0].value
    aColor = (list(reversed(Color.objects.all())))[0].value
    gramasi_karbo = hitung_gramasi_karbo(aMoisture,aPH,aSunlight)
    sprayer = hitung_sprayer(aHumidity,aAnemometer,aUV)
    pemberi_pupuk = hitung_pemberi_pupuk(aRadiation,aBerat,aColor)

    aBarometer = (list(reversed(Barometer.objects.all())))[0].value
    aWind = (list(reversed(Wind.objects.all())))[0].value
    aVisibility = (list(reversed(Visibility.objects.all())))[0].value
    aStock = (list(reversed(Stock.objects.all())))[0].value
    aSellingrate = (list(reversed(Sellingrate.objects.all())))[0].value
    aSatisfaction = (list(reversed(Satisfaction.objects.all())))[0].value
    aOccupancy = (list(reversed(Occupancy.objects.all())))[0].value
    aAudio = (list(reversed(Audio.objects.all())))[0].value
    aSentimen = (list(reversed(Sentimen.objects.all())))[0].value
    aircon = hitung_aircon(aBarometer,aWind,aVisibility)
    hasil_penjualan = hitung_hasil_penjualan(aStock,aSellingrate,aSatisfaction)
    jumlah_kursi = hitung_jumlah_kursi(aOccupancy,aAudio,aSentimen)

    output_produk = hitung_output_produk(milking_machine,slaughter_machine,feeding_machine)
    hasil_tanam = hitung_hasil_tanam(gramasi_karbo,sprayer,pemberi_pupuk)
    proyeksi_keuntungan = hitung_proyeksi_keuntungan(aircon,hasil_penjualan,jumlah_kursi)

    nilai_pabrik = hitung_nilai_pabrik(output_produk,hasil_tanam,proyeksi_keuntungan)
    return milking_machine,slaughter_machine,feeding_machine,gramasi_karbo,sprayer,pemberi_pupuk,aircon,hasil_penjualan,jumlah_kursi,output_produk,hasil_tanam,proyeksi_keuntungan,nilai_pabrik

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