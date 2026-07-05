'''
 * Archivo         : A6MP
 * Versión Thonny  : Thonny 5.0.0
'''
# Importa modulos Pin y ADC
from machine import ADC,Pin
import time

adc=ADC(Pin(33))			#Configurar el pin GPIO 33 como pin de entrada del ADC
adc.atten(ADC.ATTN_11DB)	#configura el rango de tensión entre 0 y 3.3V
adc.width(ADC.WIDTH_12BIT)	#Configura la resolución del ADC
R = Pin(23,Pin.OUT)   # Establece IO23 como pin de control del LED rojo
Y = Pin(26,Pin.OUT)   # Establece IO23 como pin de control del LED amarillo
G = Pin(27,Pin.OUT)   # Establece IO23 como pin de control del LED verde

while True:					
    boton = adc.read() 	#Lee el valor ADC del pin GPIO33 (ADKey) y lo asigna a boton
    if boton > 3500:	#determina si el valor es mayor de 3500. Si lo es imprime y enciende rojo
        print("Rojo")
        R.on()
    elif (boton > 2000) and (boton < 3000):	#comprueba 2000<boton<3000. Si es cierto imprime y enciende amarillo
        print("Amarillo")
        Y.on()
    elif boton > 900 and boton < 1500:	#comprueba 900<boton<1500. Si es cierto imprimer y enciende verde
        print("Verde")
        G.on()
    time.sleep(1)
    R.off()
    Y.off()
    G.off()
