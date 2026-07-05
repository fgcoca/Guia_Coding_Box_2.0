'''
 * Archivo         : P8MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,ADC
import time

ADkey = ADC(Pin(33))			#entrada ADC pin GPIO 33
ADkey.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
ADkey.width(ADC.WIDTH_12BIT)	#resolución ADC

#pines de control del motor IO18 e IO17
INB = Pin(18,Pin.OUT)
INA = Pin(17,Pin.OUT)

while True:
    valorBoton = ADkey.read()	#lee el valor analógico del botón pulsado
    #determina si se ha pulsado el rojo y si es cierto el motor se para
    if valorBoton > 3500:
        INB.off()
        INA.off()
    #determina si se ha pulsado el amarillo y si es cierto el motor gira
    elif valorBoton > 2000 and valorBoton < 3000:
        INB.on()
        INA.off()
    time.sleep_ms(300)

