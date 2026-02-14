# Noise Detector: Monitorización Acústica Inteligente

Sistema IoT diseñado para la monitorización en tiempo real de niveles de ruido en entornos educativos. Utiliza un **ESP32** para capturar datos, procesarlos en el "Edge" y enviarlos a una base de datos **InfluxDB** mediante una API REST.

## Características
- **Procesamiento en el borde (Edge Computing):** Filtrado de señal mediante promedios de 20 muestras para estabilizar métricas.
- **Arquitectura Escalable:** Capacidad para gestionar múltiples aulas mediante el uso de etiquetas (*tags*).
- **Backend Robusto:** Despliegue de InfluxDB mediante **Docker**.
- **Visualización:** Dashboard interactivo para análisis histórico y detección de picos de ruido.

## Hardware Necesario
- **Microcontrolador:** ESP32 DevKit V1.
- **Sensor:** Módulo de sonido de alta sensibilidad KY-037.
- **Conexiones:**
  - `VCC` -> 5V / VIN
  - `GND` -> GND
  - `AO` (Salida Analógica) -> Pin **G33** del ESP32.



## 💻onfiguración del Software

### 1. Servidor (Backend)
El sistema utiliza InfluxDB v2. Asegúrate de tener **Docker** instalado y lanza el contenedor:
```bash
docker run -d -p 8086:8086 --name influxdb influxdb:latest
