'''
 * Archivo         : P16MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
from machine import Pin,PWM
from oled import OLED
import time

# Inicializa interface I2C
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

oled = OLED(i2c)

# pines de control del sensor de ultrasonidos
Trigger = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distancia = 0
VelocidadSonido = 340

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

while True:
    distancia = obtenDistancia()
    oled.clear()
    oled.show_text("Distancia medida:", 0, 0)
    #Usa str() para convertir el valor de distancia en una cadena
    oled.show_text(str(distancia), 40, 20)
    oled.show_text("cm", 70, 20)
    oled.oled.show()
    time.sleep(1)


