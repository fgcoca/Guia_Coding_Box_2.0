'''
 * Archivo         : A14_amp_MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
import time
#importa Servo des la libreria servo
from servo import Servo

servo = Servo(pin=25)  # Pin al que está conectado el servo

while True:
    #gira gradualmente el servo de 0 a 180 grados
    for angulo in range(0,181): #recorre los números entre 0 y 180
        servo.set_angle(angulo)
        time.sleep_ms(10)
    #gira gradualmente el servo de 180 a 0 grados
    time.sleep_ms(500)
    for angulo in range(180,-1,-1): #recorre los números entre 180 y 0
        servo.set_angle(angulo)
        time.sleep_ms(10)
    time.sleep_ms(500)


