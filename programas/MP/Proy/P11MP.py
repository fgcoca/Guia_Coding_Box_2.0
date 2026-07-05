'''
 * Archivo         : P11MP
 * Versión Thonny  : Thonny 5.0.0
'''
#importa I2C y Pin desde el módulo machine
from machine import I2C, Pin
#importa AHT20 desde la libreria aht20
from aht20 import AHT20
import time
#crea objeto I2C y los pines SDA y SCL
i2c = I2C(scl=Pin(22), sda=Pin(21))
#crea un objeto AHT20, inicializa el objeto I2C para comunicarse con el sensor
sensor = AHT20(i2c)

PIR = Pin(19,Pin.IN)
INB = Pin(18,Pin.OUT)
INA = Pin(17,Pin.OUT)

while True:	
    try:
        #almacena la temperatura y la humedad en las variables
        temperatura, humedad = sensor.read_temperature_humidity()
        pir = PIR.value()
        '''
        Determina si PIR detecta personas y la temperatura supera 25 grados.
        Si es cierto el ventilador gira y si no lo es permanece parado.
        '''
        if pir == 1 and temperatura > 25:
            INB.on()
            INA.off()
        else:
            INB.off()
            INA.off()
    #detecta y lee el sensor e imprime "Fallo de lectura del sensor:"
    #si hay un error de lectura.
    except RuntimeError as e:
        print("Fallo de lectura del sensor: ", e)
    time.sleep(1)
