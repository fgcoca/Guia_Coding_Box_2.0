'''
 * Archivo         : A1MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin # Importa la clase Pin para trabajar con GPIO
import time # Para funciones de retardo

led = Pin(23,Pin.OUT) 	# Establece IO23 como pin de control del LED rojo

#Bucle infinito, para que el código se pueda ejecutar repetidamente
while True:
    led.on()			#LED rojo encendido
    time.sleep(1)		#Retardo de 1 segundo
    led.off()			#LED rojo apagado
    time.sleep(1)		#Retardo de 1 segundo