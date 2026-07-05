'''
 * Archivo         : A14MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
import time
#importa Servo des la libreria servo
from servo import Servo

servo = Servo(pin=25)  # Pin al que está conectado el servo

while True:
    # Establecer ángulo
    servo.set_angle(0)  # gira el servo a 0 grados
    time.sleep(1)
    servo.set_angle(90)  # gira el servo a 90 grados
    time.sleep(1)
    servo.set_angle(180)  # gira el servo a 180 grados
    time.sleep(1)

