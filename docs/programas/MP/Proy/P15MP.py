'''
 * Archivo         : P15MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,ADC
import machine 
import time
from servo import Servo

servo = Servo(pin=25)  # pin del servo

eje_x=ADC(Pin(35))	#Asigna la entrada del eje X del joystick a IO35
eje_x.atten(ADC.ATTN_11DB)
eje_x.width(ADC.WIDTH_12BIT)

while True:
    valor = eje_x.read()
    print("Valor analógico eje X: ", valor)
    if valor > 3500:
        servo.set_angle(0)
    elif valor < 500:
        servo.set_angle(180)
    time.sleep(3)
