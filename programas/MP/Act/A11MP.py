'''
 * Archivo         : A11MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
import math #para calculos matematicos
#importa BMP388 desde la libreria BMP388
from bmp388 import BMP388 
import time

'''
Crea un objeto BMP388 y defines los pines SDA y SCL.
Establece la frecuencia del I2C en 100KHz
'''
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)

'''
Crear un objeto BMP388, pasandole el objeto I2C creado anteriormente
para comunicarse con el sensor BMP388 a través del bus I2C.
Establece la dirección I2C del BMP388 en 0x76.
'''
bmp = BMP388(i2c, i2c_addr=0x76)

# Ajuste de Presión de Referencia al Nivel del Mar (en hPa)
P0 = 1013.25 

def calcular_altitud(presion_hpa, presion_mar_hpa):
    """Calcula la altura estimada en metros mediante la fórmula barométrica"""
    # Exponente oficial aproximado: 1 / 5.255 = 0.190284
    altitud = 44330.77 * (1.0 - math.pow(presion_hpa / presion_mar_hpa, 0.190294957))
    return altitud

while True:
    # lee la temperatura
    temperatura = round(bmp.read_temperature(), 1)
    # lee la presion
    presion = bmp.read_pressure()/100 #Divide por 100 para pasar Pa a hPa
    altitud = calcular_altitud(presion, P0)
    # Muestra los valores medidos
    print(f"Temperatura: {temperatura:.2f} °C  --  Presión: {presion:.2f} hPa  --  Altitud: {altitud:.2f} m")
    time.sleep(1)


