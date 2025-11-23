import time

from sensores.dht_sensor import leer_temperatura
from sensores.promedio import calcular_promedio
from wifi.wifi_manager import conectar_wifi, enviar_dato
from alarmas.alarma_temp import verificar_alarma
from registro.logger import guardar_en_log

# ==========================
# CONFIGURACIÓN DEL SISTEMA
# ==========================

SSID = "TU_SSID"                  # <- cámbialo por tu red WiFi
PASSWORD = "TU_PASSWORD"          # <- cámbialo por tu clave
URL_SERVIDOR = "http://ejemplo.com/api/temperatura"  # <- endpoint de tu API
LIMITE_TEMPERATURA = 30           # °C - umbral de alarma
CANTIDAD_LECTURAS = 10            # cuántas lecturas usar para el promedio
INTERVALO_SEGUNDOS = 5            # cada cuánto leer el sensor


def iniciar():
    print("=== Sistema de monitoreo térmico ESP32 ===")
    print("Conectando a WiFi...")
    conectar_wifi(SSID, PASSWORD)
    print("WiFi OK. Iniciando ciclo de monitoreo...")
    ciclo_monitoreo()


def ciclo_monitoreo():
    lecturas = []

    while True:
        try:
            temp = leer_temperatura()
            print("📡 Lectura actual:", temp, "°C")
            lecturas.append(temp)

            # Cuando juntamos suficientes lecturas, procesamos
            if len(lecturas) >= CANTIDAD_LECTURAS:
                promedio = calcular_promedio(lecturas)
                print("📊 Promedio de las últimas", CANTIDAD_LECTURAS, "lecturas:", promedio, "°C")

                # Guardar en log local
                guardar_en_log(promedio)

                # Verificar alarmas
                verificar_alarma(promedio, LIMITE_TEMPERATURA)

                # Intentar enviar al servidor
                try:
                    enviar_dato(URL_SERVIDOR, promedio)
                except Exception as e:
                    print("⚠️ Error enviando dato al servidor:", e)

                # Reiniciar buffer de lecturas
                lecturas = []

        except Exception as e:
            print("⚠️ Error leyendo sensor:", e)

        time.sleep(INTERVALO_SEGUNDOS)


# Punto de entrada
if __name__ == "__main__":
    iniciar()
