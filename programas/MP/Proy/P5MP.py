'''
 * Archivo         : P5MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import ADC,Pin
import time
#importa Servo de la libreria servo
from servo import Servo

servo = Servo(pin=25)  #pin de control IO25

adc=ADC(Pin(36))			#entrada ADC pin GPIO 36
adc.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#resolución ADC

while True:
    luminosidad = adc.read()
    if luminosidad < 500:	#determina si la luminosidad es menor de 500
        servo.set_angle(180)  # gira un ángulo de 180 grados
    else:
        servo.set_angle(0)  # gira un ángulo de 0 grados
    time.sleep_ms(300)
