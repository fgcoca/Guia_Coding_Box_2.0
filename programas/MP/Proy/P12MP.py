'''
 * Archivo         : P12MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
#importa I2C y Pin desde el módulo machine
from machine import I2C, Pin
#importa AHT20 desde la libreria aht20
from aht20 import AHT20
#importa BMP388 desde la libreria BMP388
from bmp388 import BMP388
from oled import OLED
import time

#crea objeto I2C y los pines SDA y SCL
i2c = I2C(scl=Pin(22), sda=Pin(21))
#crea un objeto AHT20, inicializa el objeto I2C para comunicarse con el sensor
sensor = AHT20(i2c)

#crea un objeto BMP388 y establece los pines SCL y SDA, establece la frecuencia en 100KHz
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)

#crea un objeto BMP388, inicializa el objeto I2C para comunicarse con el sensor
bmp = BMP388(i2c, i2c_addr=0x76)

# crea ejemplo OLED
oled = OLED(i2c)
# borra oled
oled.clear()

'''
La función str() convierte una variable de tipo cadena a partir de una variable
de otro tipo. 

La función int() convierte una variable de otro tipo a una variable de tipo
entero. El motivo de esta conversión es que no se muestran los datos tras la
conversión de la unidad de presión decimal: 1 hPa = 1 × 100 Pa = 100 Pa
'''

while True:
    try:
        #almacena la temperatura y la humedad en las variables
        temperatura, humedad = sensor.read_temperature_humidity()
        # lee la presión.
        presion = bmp.read_pressure() // 100 #Convierte Pa a hPa dividiendo la presion entre 100        
        # borra pantalla
        oled.clear()
        # muestra la presión
        oled.show_text("Presion:", 0, 0)
        oled.show_text(str(int(presion)), 70, 0)
        oled.show_text("hPa", 105, 0)
        # muestra la temperatura
        oled.show_text("Temperatura:", 0, 15)
        oled.show_text(str(int(temperatura)), 100, 15)
        oled.show_text("C", 120, 15)
        # muestra la humedad
        oled.show_text("Humedad:", 0, 30)
        oled.show_text(str(int(humedad)), 75, 30)
        oled.show_text("%", 105, 30)

        # muestra oled
        oled.oled.show()
    # detect and read value, print “Failed to read from sensor:” if an error occurs
    except RuntimeError as e:
        print("Fallo de lectura del sensor: ", e)
    time.sleep(1)


