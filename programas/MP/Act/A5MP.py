'''
 * Archivo         : A4MP
 * Versión Thonny  : Thonny 5.0.0
'''
# Importa modulos Pin, ADC y DAC .
from machine import ADC,Pin,DAC
import time

adc=ADC(Pin(36))			#Configurar el pin GPIO 36 como pin de entrada del ADC
adc.atten(ADC.ATTN_11DB)	#configura el rango de tensión entre 0 y 3.3V
adc.width(ADC.WIDTH_12BIT)	#Configura la resolución del ADC

while True:				
    Val_adc=adc.read()	#Lee el valor del sensor y lo asigna a la variable Val_adc
    print("ADC Val:",Val_adc)	#Imprime el valor de Val_adc
    time.sleep(0.5)				#retardo de 0.5s
