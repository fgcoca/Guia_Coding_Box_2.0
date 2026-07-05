'''
 * Archivo         : P4MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,PWM
import time

#Establece el pin, la frecuencia y el ciclo de trabajo del 50% del PWM
altavoz = PWM(Pin(32), freq=5000, duty=128)

LEDrojo = Pin(23,Pin.OUT)
LEDverde = Pin(27,Pin.OUT)
pir = Pin(19,Pin.IN)

while True:
    #lee el valor del sensor PIR y lo asigna a la variable PIR
    PIR = pir.value()
    print("PIR:",PIR)	#imprime en la consola el valor de la variable PIR
    if PIR == 1:		#determina si PIR = 1
        LEDverde.off()	#apaga el verde
        LEDrojo.on()	#enciende rojo
        altavoz.duty(50)	#ciclo de trabajo del altavoz al 50%
        altavoz.freq(880)	#frecuencia del altavoz
    else:
        LEDrojo.off()	#apaga rojo
        LEDverde.on()	#enciende verde
        altavoz.duty(0)	#ciclo de trabajo del altavoz al 0%, detiene el sonido
    time.sleep(0.1)
