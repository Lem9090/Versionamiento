import dht
from machine import Pin

sensor = dht.DHT22(Pin(4))

def leer_temperatura():
    sensor.measure()
    return sensor.temperature()
