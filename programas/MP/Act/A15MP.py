'''
 * Archivo         : A15MP
 * Versión Thonny  : Thonny 5.0.0
'''
#importa módulos necesarios: Pin, neopiexl y time.
from machine import Pin
import neopixel
import time

pin = Pin(16, Pin.OUT) #define el pin de control SK6812 como IO16
num_pixels = 12	#Establece el número de LEDs SK6812 en 12
#inicializa SK6812
np = neopixel.NeoPixel(pin, num_pixels)

rojo = [255,0,0] #establece el color en rojo

while True:
    np[10] = rojo #el primer LED se ilumina en rojo. 12 LEDS: números del 0 al 11
    np.write() #muestra el color en el LED
    
