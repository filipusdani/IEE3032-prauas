from rest_framework.response import Response
from .serializers import SensorSerializer
from .models import Sensor

dev = False

def on_message_temperature(client, userdata, msg):
    temperature = Sensor.objects.get(name="temperature")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(temperature, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print("=============================================================")
            print('recieved a new temperature data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_conductivity(client, userdata, msg):
    conductivity = Sensor.objects.get(name="conductivity")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(conductivity, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new conductivity data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_flow(client, userdata, msg):
    flow = Sensor.objects.get(name="flow")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(flow, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new flow data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_co(client, userdata, msg):
    co = Sensor.objects.get(name="co")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(co, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new co data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_amonia(client, userdata, msg):
    amonia = Sensor.objects.get(name="amonia")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(amonia, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new amonia data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_pressure(client, userdata, msg):
    pressure = Sensor.objects.get(name="pressure")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(pressure, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new pressure data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_o2(client, userdata, msg):
    o2 = Sensor.objects.get(name="o2")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(o2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new o2 data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_co2(client, userdata, msg):
    co2 = Sensor.objects.get(name="co2")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(co2, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new co2 data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_waterlevel(client, userdata, msg):
    waterlevel = Sensor.objects.get(name="waterlevel")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(waterlevel, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new waterlevel data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_moisture(client, userdata, msg):
    moisture = Sensor.objects.get(name="moisture")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(moisture, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new moisture data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_ph(client, userdata, msg):
    ph = Sensor.objects.get(name="ph")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(ph, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new ph data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_sunlight(client, userdata, msg):
    sunlight = Sensor.objects.get(name="sunlight")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(sunlight, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new sunlight data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_humidity(client, userdata, msg):
    humidity = Sensor.objects.get(name="humidity")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(humidity, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new humidity data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_anemometer(client, userdata, msg):
    anemometer = Sensor.objects.get(name="anemometer")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(anemometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new anemometer data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_uv(client, userdata, msg):
    uv = Sensor.objects.get(name="uv")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(uv, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new uv data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_radiation(client, userdata, msg):
    radiation = Sensor.objects.get(name="radiation")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(radiation, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new radiation data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_berat(client, userdata, msg):
    berat = Sensor.objects.get(name="berat")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(berat, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new berat data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_color(client, userdata, msg):
    color = Sensor.objects.get(name="color")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(color, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new color data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_barometer(client, userdata, msg):
    barometer = Sensor.objects.get(name="barometer")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(barometer, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new barometer data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_wind(client, userdata, msg):
    wind = Sensor.objects.get(name="wind")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(wind, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new wind data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_visibility(client, userdata, msg):
    visibility = Sensor.objects.get(name="visibility")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(visibility, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new visibility data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_stock(client, userdata, msg):
    stock = Sensor.objects.get(name="stock")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(stock, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new stock data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_sellingrate(client, userdata, msg):
    sellingrate = Sensor.objects.get(name="sellingrate")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(sellingrate, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new sellingrate data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_satisfaction(client, userdata, msg):
    satisfaction = Sensor.objects.get(name="satisfaction")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(satisfaction, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new satisfaction data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_occupancy(client, userdata, msg):
    occupancy = Sensor.objects.get(name="occupancy")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(occupancy, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new occupancy data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_audio(client, userdata, msg):
    audio = Sensor.objects.get(name="audio")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(audio, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new audio data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})

def on_message_sentimen(client, userdata, msg):
    sentimen = Sensor.objects.get(name="sentimen")
    data = {'value': msg.payload.decode('utf-8')}
    serializer = SensorSerializer(sentimen, data=data, partial=True)
    if serializer.is_valid():
        serializer.save()
        if dev:
            print('recieved a new sentimen data ', msg.payload.decode('utf-8'))    
    return Response({"value": msg.payload.decode('utf-8')})
