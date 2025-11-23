import network
import urequests

def conectar_wifi(ssid, password):
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while not wlan.isconnected():
        pass
    print("Conectado a WiFi:", wlan.ifconfig())

def enviar_dato(url, temperatura):
    data = {"temperatura": temperatura}
    respuesta = urequests.post(url, json=data)
    print("Respuesta del servidor:", respuesta.text)
