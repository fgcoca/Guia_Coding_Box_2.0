'''
 * Archivo         : A12MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin
#importa ak8975c desde AK8975C
from AK8975C import ak8975c
import time

scl = Pin(22)
sda = Pin(21)
#crea un objeto ak8975c e inicializa los pines SCL y SDA del bus I2C
Triaxial = ak8975c(scl, sda)

while True:
    Triaxial.measure()  # mide los valores
    # Muestra la magnitud geomagnética de los ejes XYZ
    print('x:',Triaxial.X,'y:',Triaxial.Y,'z:',Triaxial.Z)
    # Muestra el valor del ángulo del rumbo solo si dicho ángulo se puede calcular
    if Triaxial.AK8975_GET_AZIMUTH(Triaxial.X, Triaxial.Y) == True:  
        print('Rumbo:', Triaxial.angle_val,'°')
    time.sleep(3)
