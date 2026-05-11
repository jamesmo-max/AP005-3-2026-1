# 📡 Monitoreo de Potenciómetro con ESP32, Flask y Chart.js

## 🧠 Descripción del proyecto

Este proyecto consiste en la lectura de un potenciómetro usando un ESP32, el envío de datos mediante WiFi hacia un servidor desarrollado con Flask y su visualización en tiempo real desde una interfaz web usando Chart.js.

El sistema integra conceptos de:

- Electrónica
- IoT
- Programación embebida
- Backend con Python
- Desarrollo web
- Visualización de datos en tiempo real

---

# ⚙️ Tecnologías utilizadas

- ESP32
- MicroPython
- Python 3
- Flask
- Flask-CORS
- Requests
- HTML5
- JavaScript
- Chart.js

---

# 🔄 Funcionamiento del sistema

1. El potenciómetro genera una señal analógica.
2. El ESP32 convierte la señal a un valor digital (0 - 4095).
3. El ESP32 crea un servidor HTTP y envía el dato por WiFi.
4. El servidor Flask recibe el valor del ESP32.
5. El frontend consulta el servidor Flask cada 200 ms.
6. La gráfica se actualiza en tiempo real desde el navegador.

---

# 📂 Estructura del proyecto

```bash
esp32-pot-monitor/
│
├── esp32/
│   └── main.py
│
├── backend/
│   └── app.py
│
├── frontend/
│   └── index.html
│
├── README.md
│
└── requirements.txt
```

---

# 📜 Explicación de archivos

## 📌 `esp32/main.py`

Código ejecutado en el ESP32:

- Conexión WiFi
- Lectura ADC
- Servidor HTTP
- Envío del valor del potenciómetro

---

## 📌 `backend/app.py`

Servidor Flask encargado de:

- Solicitar datos al ESP32
- Validar respuestas
- Exponer endpoint `/dato`
- Permitir conexión CORS

---

## 📌 `frontend/index.html`

Interfaz web que:

- Consulta datos automáticamente
- Grafica valores en tiempo real
- Usa Chart.js para visualización

---

# ▶️ Ejecución del proyecto

## 1️⃣ Configurar ESP32

Cargar el archivo:

```bash
esp32/main.py
```

---

## 2️⃣ Ejecutar servidor Flask

Ir a:

```bash
backend/
```

Instalar dependencias:

```bash
pip install flask flask-cors requests
```

Ejecutar:

```bash
python app.py
```

---

## 3️⃣ Abrir interfaz web

Abrir:

```bash
frontend/index.html
```

o usar Live Server en Visual Studio Code.

---

# 📊 Resultados

El sistema permite visualizar:

✅ Lectura en tiempo real del potenciómetro  
✅ Comunicación WiFi con ESP32  
✅ Actualización automática de datos  
✅ Gráfica dinámica en tiempo real  
✅ Integración IoT completa

---

# 🌐 Arquitectura del sistema

```text
Potenciómetro
      ↓
ESP32 (ADC)
      ↓ WiFi
Servidor Flask
      ↓ HTTP
Frontend Web
      ↓
Gráfica en tiempo real
```

---

# 🚀 Posibles mejoras

- Guardar datos en base de datos
- Dashboard profesional
- WebSocket para tiempo real
- Sensores múltiples
- Integración con MQTT
- Deploy en Raspberry Pi

---

# 👨‍💻 Autor

Proyecto académico de IoT y visualización de datos usando ESP32, Flask y Chart.js.
