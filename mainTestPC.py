import requests 
import time
import random

# ======================
# CONFIGURACIÓN
# ======================
INFLUX_URL = "http://localhost:8086/api/v2/write" 
INFLUX_TOKEN = "tvM747Qn6Z1nXUp9Qcdv1K0f-1xMR4Atil_MAzHx3iF_MDj9NaHbi8fOB3PGONctNncEd0z_XWvYjX4uOkr9fA=="
INFLUX_ORG = "juanjosejm" 
INFLUX_BUCKET = "noiseLevel"

AULAS_TEST = [210, 211, 212, 213]

# ======================
# INFLUXDB
# ======================
def enviar_influx(aula, valor):
    headers = {
        "Authorization": "Token " + INFLUX_TOKEN,
        "Content-Type": "text/plain; charset=utf-8"
    }

    data = "noiselevel,classroom={} valor={}".format(aula, valor)
    endpoint = "{}?org={}&bucket={}&precision=s".format(
        INFLUX_URL, INFLUX_ORG, INFLUX_BUCKET
    )

    try:
        r = requests.post(endpoint, headers=headers, data=data, timeout=5)
        
        if r.status_code == 204:
            print(f"Aula {aula}: Enviado valor {valor}")
        else:
            print(f"Error {r.status_code}: {r.text} (Aula {aula})")
        
        r.close()
    except Exception as e:
        print(f"Error de conexión: {e}")

# ======================
# PROGRAMA PRINCIPAL
# ======================
print(f"Iniciando simulación en organización: {INFLUX_ORG}...")

while True:
    for aula in AULAS_TEST:
        if aula == 210: valor = random.randint(350, 450)
        elif aula == 211: valor = random.randint(600, 850)
        elif aula == 212: valor = random.randint(150, 300)
        else: valor = random.randint(200, 700)

        enviar_influx(aula, valor)
    
    print("-" * 45)
    time.sleep(5)