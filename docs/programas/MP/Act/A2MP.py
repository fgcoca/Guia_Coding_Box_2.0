'''
 * Archivo         : A2MP
 * Versión Thonny  : Thonny 5.0.0
'''
# Importar módulos Pin, ADC y DAC.
from machine import ADC,Pin
import time

adc=ADC(Pin(34))			#Establece el pin GPIO 34 como pin de entrada ADC
# Aplica atenuación de 11dB para reducir señal de entrada y permitir voltajes hasta 3.6V
adc.atten(ADC.ATTN_11DB)	#Rango de tensión 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#Establece a 12 bits la resolución del ADC

'''
Lee el valor del ADC una vez cada 50 ms 
Convierte el valor del ADC en un valor del DAC
Envía e imprime estos datos en la consola.
'''
while True:
    # Lee el valor analógico del sensor de sonido y asígnalo a la variable "V_adc"
    V_adc = adc.read()
    print("Valor del ADC de sonido:",V_adc) #imprime el valor de V_adc en el monitor serie
    time.sleep_ms(50) #retarde de 50ms
