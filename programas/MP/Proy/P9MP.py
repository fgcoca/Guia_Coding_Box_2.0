'''
 * Archivo         : P9MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin
import time
from servo import Servo

PIR = Pin(19,Pin.IN)
servo = Servo(pin=25)

while True:
    pir = PIR.value()
    if pir == 1:
        servo.set_angle(180)  # servo a 180 grados. Puerta abierta
    else:
        servo.set_angle(0)  # servo a 0 grados. Puerta cerrada
    time.sleep_ms(300)
    
