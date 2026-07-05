'''
 * Archivo         : A3MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin
import time

PIR = Pin(19, Pin.IN)  # Configurar el pin IO19 como pin de entrada PIR
while True:				
    valor_PIR = PIR.value()	#Lee el valor del sensor PIR y lo asigna a la variable
    print(valor_PIR, end = " ") #Imprimir el valor de PIR sin salto de línea
    if valor_PIR == 1:		#determinar si valor_PIR = 1
        print("¡Hay alguien por aquí!")#si valor_PIR = 1 es muestra el mensaje
    else:	#o si no
        print("¡Nadie!")
    time.sleep(0.1)	#retardo de 0.1s (100ms)
    