from machine import Pin

led = Pin(2, Pin.OUT)

def verificar_alarma(temp, limite):
    if temp > limite:
        led.value(1)
        print("⚠️ ALARMA: Temperatura demasiado alta")
    else:
        led.value(0)
