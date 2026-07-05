'''
 * Archivo         : P19MP
 * Versión Thonny  : Thonny 5.0.0
'''
import network
import socket
import time
import json
import machine
from machine import Pin, ADC, I2C,SoftI2C,PWM
import aht20

# Conexión WiFi 2.4 GHz
SSID = 'nombre de tu WiFi'  # nombre de tu WiFi
PASSWORD = 'contraseña de tu WiFi'  # contraseña de tu WiFi

# inicializa LDR
light_sensor = ADC(Pin(36))
light_sensor.atten(ADC.ATTN_11DB)

# sensor ultrasonidos
Trigger = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distancia = 0
VelocidadSonido = 340

# PIR sensor
pir_sensor = Pin(19, Pin.IN)

# sensor AHT20 
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
aht20Sensor = aht20.AHT20(i2c)

def obtenDistancia():
    Trigger.value(1)
    time.sleep_us(10) #para habilitar el sensor de ultrasonidos
    Trigger.value(0)
    while Echo.value() == 0:
        Inicio = time.ticks_us()
    while Echo.value() == 1:
        Fin = time.ticks_us()
    Tiempo = time.ticks_diff(Fin,Inicio)
    distancia =  Tiempo * VelocidadSonido //2 // 10000
    return distancia

def connect_wifi(ssid, password):
    # Crea objeto WLAN usando el modo STA (modo cliente)
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)  # activa la interface WLAN
    wlan.connect(ssid, password)  # Conecta a la red WiFi especificada

    timeout = 10  # Duración del tiempo de espera de conexión en segundos
    '''
    Si la conexión falla y el tiempo de espera aún no ha vencido, comprueba
    de nuevo el estado de la conexión
    '''
    while not wlan.isconnected() and timeout > 0:
        print("Conectando a la red WiFi...")
        time.sleep(1)
        timeout -= 1

    '''
    Si la conexión no se establece tras agotarse el tiempo de espera, se
    lanza una excepción
    '''
    if not wlan.isconnected():
        raise Exception("No es posible conectar a WiFi")
    '''
    Configuración de la red:
    dirección IP, máscara de subred, puerta de enlace y DNS
    '''
    print('Configuración de la red:', wlan.ifconfig())
    # Mostrar la dirección IP de la conexión establecida con éxito
    print('Conectado a WiFi, dirección IP:', wlan.ifconfig()[0])  
    return wlan

# crea página HTML
def web_page():
    html = """<html>
    <head>
        <title>Datos sensores ESP32 Coding Box 2.0</title>
        <style>
            body { font-family: Arial, sans-serif; text-align: center; }
            .sensor { font-size: 24px; margin-top: 20px; }
        </style>
        <script>
            function updateData() {
                fetch('/sensor_data').then(function(response) {
                    return response.json();
                }).then(function(data) {
                    document.getElementById('light').innerText = data.light;
                    document.getElementById('distance').innerText = data.distance;
                    document.getElementById('pir').innerText = data.pir ? "Intruso detectado" : "No hay nadie";
                    document.getElementById('temperature').innerText = Number(data.temperature).toFixed(2);
                    document.getElementById('humidity').innerText = Number(data.humidity).toFixed(2);
                });
            }
            setInterval(updateData, 1000);
        </script>
    </head>
    <body>
        <h1>Datos sensores ESP32 Coding Box 2.0</h1>
        <div class="sensor">Sensor luz (LDR): <span id="light"></span></div>
        <div class="sensor">Distancia: <span id="distance"></span> cm</div>
        <div class="sensor">Sensor PIR: <span id="pir"></span></div>
        <div class="sensor">Temperatura: <span id="temperature"></span> *C</div>
        <div class="sensor">Humedad: <span id="humidity"></span> %</div>
    </body>
    </html>"""
    return html  # retorna la página html que contiene los datos

# Iniciar servidor web
def start_server():
    wlan = connect_wifi(SSID, PASSWORD)  # conecta a WiFi
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]  # obtiene la IP local y el puerto 80
    s = socket.socket()  # Crea un objeto socket
    s.bind(addr)  # Asignar sockets a direcciones y puertos
    s.listen(5)  # Empieza a escuchar las conexiones entrantes. El número máximo de conexiones es de 5.
    print('Escuchando en', addr)  # Imprime la dirección y el puerto

    while True:
        cl, addr = s.accept()  # Aceptar una conexión de cliente
        print('El cliente se ha conectado desde', addr)  # Imprime la dirección del cliente
        request = cl.recv(1024)  # Recibir solicitudes de los clientes, de hasta 1024 bytes
        request = str(request)  # Convertir la solicitud en una cadena
        print('Contenido de la solicitud = %s' % request)  # Imprimir contenido de la solicitud
        
        if 'GET /sensor_data' in request:
            light_value = light_sensor.read()
            distance = obtenDistancia()
            pir_value = pir_sensor.value()
            temperature, humidity = aht20Sensor.read_temperature_humidity()

            sensor_data = {
                'light': light_value,
                'distance': distance,
                'pir': pir_value,
                'temperature': temperature,
                'humidity': humidity
            }

            response = 'HTTP/1.1 200 OK\nContent-Type: application/json\n\n'
            response += json.dumps(sensor_data)
            cl.send(response)
        else:
            response = web_page()
            cl.send('HTTP/1.1 200 OK\n')
            cl.send('Content-Type: text/html\n')
            cl.send('Connection: close\n\n')
            cl.sendall(response)
        cl.close()

# Ejecutar el servidor
try:
    start_server()  # Intenta iniciar el servidor web
except Exception as e:
    # Si el inicio falla, aparece un mensaje de error
    print('No se ha podido iniciar el servidor:', e)  
    machine.reset()  # Reinicia el dispositivo para intentar volver a conectarte
