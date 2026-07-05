'''
 * Archivo         : P6MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,ADC
import time

luminosidad = ADC(Pin(36))  #entrada ADC pin GPIO 36
luminosidad.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
luminosidad.width(ADC.WIDTH_12BIT)	#resolución ADC

sonido = ADC(Pin(34))
sonido.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
sonido.width(ADC.WIDTH_12BIT)	#resolución ADC

led = Pin(23,Pin.OUT)

while True:
    '''
    Lee el valor del sensor de luz y comprueba si es inferior a 500.
    Si no es así, sale del bucle.
    '''
    while luminosidad.read() < 500:
        '''
        Lee el valor del sensor de sonido y comprueba si es superior a 200.
        Si es así, enciende el LED durante 5 s.
        '''
        if sonido.read() > 200:
            led.on()
            time.sleep(5)
            led.off()
