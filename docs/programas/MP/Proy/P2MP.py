'''
 * Archivo         : P2MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin, PWM  
import time  
  
# Establece el pin y la frecuencia del PWM  
pwm_pin = Pin(23, Pin.OUT)  
pwm = PWM(pwm_pin, freq=1000)  # frecuencia de 1000Hz  
  
# parpadeo del LED  
while True:  
    for duty in range(0, 1024, 5):  # aumenta luminosidad gradualmente
        pwm.duty(duty)  
        time.sleep_ms(10)  # peuqeño retardo para observar mejor el efecto  
    for duty in range(1023, -1, -5):  # apagado gradual
        pwm.duty(duty)  
        time.sleep_ms(10)
