'''
 * Archivo         : A10MP
 * Versión Thonny  : Thonny 5.0.0
'''
#importa pines e I2C desde machine
from machine import I2C, Pin
#importa AHT20 desde la libreria aht20
from aht20 import AHT20
import time
#crea un objeto I2C y defines los pines SDA y SCL
i2c = I2C(scl=Pin(22), sda=Pin(21))
'''
Crear un objeto AHT20 e inicializa el objeto I2C para comunicarse a través
del bus I2C con el sensor AHT20.
'''
sensor = AHT20(i2c)

while True:	
    try:
        #Guarda los valores de temperatura y humedad en las variables "temperatura" y "humedad"
        temperatura, humrdad = sensor.read_temperature_humidity()
        #Valor de la variable formateado con dos decimales
        print("Temperatura: {:.2f} C, Humedad: {:.2f} %".format(temperatura, humrdad))
    #Lee el valor detectado; si se produce un error, muestra el mensaje "Error de lectura del sensor:"
    except RuntimeError as e:
        print("Error de lectura del sensor: ", e)
    time.sleep(1)
