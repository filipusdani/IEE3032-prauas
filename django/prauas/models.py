from django.db import models

class Temperature(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Conductivity(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Flow(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class CO(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Amonia(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Pressure(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class O2(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class CO2(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Waterlevel(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Moisture(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class PH(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Sunlight(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Humidity(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Anemometer(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class UV(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Radiation(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Berat(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Color(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Barometer(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Wind(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Visibility(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Stock(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Sellingrate(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Satisfaction(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Occupancy(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Audio(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)

class Sentimen(models.Model):
    value = models.FloatField()
    date_created = models.DateTimeField(auto_now_add=True)
