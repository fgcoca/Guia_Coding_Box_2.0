'''
 * Archivo         : P3MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,ADC
import time

led = Pin(23,Pin.OUT)
ADkey = ADC(Pin(33))			#establece el pin GPIO 33 como entrada ADC
ADkey.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
ADkey.width(ADC.WIDTH_12BIT)	#resolución del ADC
#define una variable para cambiar el estado del LED
estadoLED = False

while True:
    ValorADkey = ADkey.read()	#lee el valor analogico del boton
    if ValorADkey > 3500:	#si esmayor de 3500 indica que el botón se ha pulsado
        #Invierte el valor de estadoLED:
        #si es False pasa a ser True
        #si es True pasa a ser False.
        estadoLED = not estadoLED #invierte el estado del LED
        time.sleep_ms(500)
    #led.value() es diferente de led.on() / led.off(), ya que en led.value()
    #hay que introducir 0 (LED apagado) o 1 (LED encendido).
    led.value(estadoLED)
