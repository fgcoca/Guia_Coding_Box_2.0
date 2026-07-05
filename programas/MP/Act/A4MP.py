'''
 * Archivo         : A4MP
 * Versión Thonny  : Thonny 5.0.0
 
-------------------------------
|Notas  |     Frecuencias     |
|       | octava 4 | octava 5 |
|-----------------------------|
|C (Do) |    440     |  523   |
|D (Re) |    494     |  587   |
|E (Mi) |    523     |  659   |
|F (Fa) |    587     |  698   |
|G (So) |    659     |  784   |
|A (La) |    698     |  880   |
|B (Si) |    784     |  988   |
-------------------------------

'''
from machine import Pin, PWM
import time

'''
Configura el pin IO32 como pin de salida PWM, con una frecuencia de 5000 Hz y
un ciclo de trabajo del 50 %.
Con 8 bit el valor central de la resolución es 128
El ciclo de trabajo oscila entre 0 y 255).
'''
trompeta = PWM(Pin(32), freq=5000, duty=128) 

#define matrices para almacenar las frecuencias
f4 = [440,494,523,587,659,698,784] #octava 4
f5 = [523,587,659,698,784,880,988] #octava 5

for i in f5: #Bucle for con la matriz f: si hay n conjuntos de datos, se repiten n veces
    trompeta.duty(10) #Control del ciclo de trabajo PWM (0-255); el volumen del sonido es regulable
    trompeta.freq(i) #ajuste de la frecuencia (emitir sonido controlando la frecuencia)
    time.sleep(0.5)	#retardo de 0.5s
    trompeta.duty(0) #poner duty cycle a 0 para apagar el amplificador