'''
 * Archivo         : botones
 * Versión Thonny  : Thonny 5.0.0
'''
# Importa modulos Pin y ADC
from machine import ADC,Pin
import time

adc=ADC(Pin(33))			#Configurar el pin GPIO 33 como pin de entrada del ADC
adc.atten(ADC.ATTN_11DB)	#configura el rango de tensión entre 0 y 3.3V
adc.width(ADC.WIDTH_12BIT)	#Configura la resolución del ADC

while True:				
    Val_adc=adc.read()	#Lee el valor del sensor y lo asigna a la variable Val_adc
    print("Valor ADC GPIO33:",Val_adc)	#Imprime el valor de Val_adc
    time.sleep(3)				#retardo de 0.5s
