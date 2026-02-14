from machine import Pin, ADC
import network
import urequests
import time

# --- CONFIGURACIÓN DE PARÁMETROS ---
WIFI_SSID = "Aula211_2G"
WIFI_PASS = "internet211"
INFLUX_URL = "http://localhost:8086/api/v2/write" 
INFLUX_TOKEN = "tvM747Qn6Z1nXUp9Qcdv1K0f-1xMR4Atil_MAzHx3iF_MDj9NaHbi8fOB3PGONctNncEd0z_XWvYjX4uOkr9fA=="
INFLUX_ORG = "juanjosejm"
INFLUX_BUCKET = "noiseLevel"
CLASSROOM = 210

# --- CONFIGURACIÓN DEL HARDWARE ---
adc = ADC(Pin(33))
adc.atten(ADC.ATTN_11DB)
adc.width(ADC.WIDTH_12BIT)

# --- MÓDULO DE CONECTIVIDAD ---
def conectar_wifi():
    """Establece la conexión con el punto de acceso WiFi."""
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print("Buscando red...")
        wlan.connect(WIFI_SSID, WIFI_PASS)
        while not wlan.isconnected():
            time.sleep(0.5)
    print("Conexión establecida. IP:", wlan.ifconfig()[0])

# --- MÓDULO DE TRANSMISIÓN API REST ---
def enviar_influx(valor):
    """Construye y envía la petición HTTP POST a InfluxDB."""
    headers = {
        "Authorization": "Token " + INFLUX_TOKEN,
        "Content-Type": "text/plain; charset=utf-8"
    }

    data = "noiselevel,classroom={} valor={}".format(CLASSROOM, valor)

    url_final = "{}?org={}&bucket={}&precision=s".format(
        INFLUX_URL, INFLUX_ORG, INFLUX_BUCKET
    )

    try:
        r = urequests.post(url_final, headers=headers, data=data)
        r.close()
        print("Dato enviado exitosamente:", valor)
    except Exception as e:
        print("Fallo en la comunicación:", e)

# --- BUCLE PRINCIPAL ---
conectar_wifi()

while True:
    muestras = []
    for _ in range(20):
        muestras.append(adc.read())
        time.sleep(0.05)

    valor_promediado = sum(muestras) // len(muestras)    
    enviar_influx(valor_promediado)
    time.sleep(5)