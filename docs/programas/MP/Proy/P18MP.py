'''
 * Archivo         : P18MP
 * Versión Thonny  : Thonny 5.0.0
'''
import network
import socket
import time
import machine

# Conexión WiFi 2.4 GHz
SSID = 'nombre de tu WiFi'  # nombre de tu WiFi
PASSWORD = 'contraseña de tu WiFi'  # contraseña de tu WiFi

# conectar a WiFi
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
        <title>Servidor Web ESP32</title>
    </head>
    <body>
        <h1>Hola Mundo</h1>
    </body>
    </html>"""
    return html  # Devuelve una sencilla pagina web con el texto Hola Mundo

# Inicia el servidor Web
def start_server():
    wlan = connect_wifi(SSID, PASSWORD)  # conecta a WiFi
    
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    # Obtener la dirección IP local y el puerto 80
    s = socket.socket()  # Crea un objeto socket (dispositivo que se conecta a WiFi)
    s.bind(addr)  # Asignar sockets a direcciones y puertos
    s.listen(5)  # Empieza a escuchar las conexiones entrantes. El número máximo de conexiones es de 5.
    print('Escuchando en', addr)  # Imprime la dirección y el puerto en los que el servidor está a la escucha

    while True:
        cl, addr = s.accept()  # Aceptar una conexión de cliente
        print('El cliente se ha conectado desde', addr)  # Imprime la dirección del cliente
        request = cl.recv(1024)  # Recibir solicitudes de los clientes, de hasta 1024 bytes
        request = str(request)  # Convertir la solicitud en una cadena
        print('Contenido de la solicitud = %s' % request)  # Imprimir contenido de la solicitud
        
        response = web_page()  # Generar una respuesta HTML
        cl.send('HTTP/1.1 200 OK\n')  # Enviar la cabecera de la respuesta HTTP
        cl.send('Tipo de contenido: texto/html\n')  # Especifica el tipo de contenido como HTML
        cl.send('Conexión: cerrada\n\n')  # Cerrar conexión
        cl.sendall(response)  # Enviar el contenido de una página HTML
        cl.close()  # Cierra la conexión del cliente

# Ejecutar el servidor
try:
    start_server()  # Intenta iniciar el servidor web
except Exception as e:
    # Si el inicio falla, aparece un mensaje de error
    print('No se ha podido iniciar el servidor:', e)  
    machine.reset()  # Reinicia el dispositivo para intentar volver a conectarte
