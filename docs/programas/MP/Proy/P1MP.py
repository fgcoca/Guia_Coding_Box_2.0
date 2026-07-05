'''
 * Archivo         : P1MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin
import time

LEDrojo = Pin(23,Pin.OUT)	#IO23 es el pin del LED rojo
LEDverde = Pin(27,Pin.OUT)	#IO27 es el pin del LED verde
LEDamarillo = Pin(26,Pin.OUT)	#IO26 es el pin del LED amarillo

#apaga todos los LEDs
LEDrojo.off()
LEDverde.off()
LEDamarillo.off()

#green led on for 5S; yellow led blink for 3; red led on for 5S; in a loop
while True:
    LEDverde.on()
    time.sleep(5)
    LEDverde.off()
    for i in range(0,3):
        LEDamarillo.on()
        time.sleep(0.5)
        LEDamarillo.off()
        time.sleep(0.5)
    LEDrojo.on()
    time.sleep(5)
    LEDrojo.off()
