'''
 * Archivo         : A9MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin, ADC
import time
# Inicializa el módulo Joystick (función ADC)
pos_x=ADC(Pin(35))	#pin IO35 entrada del eje X
pos_y=ADC(Pin(39))	#pin IO39 entrada del eje Y

'''
Establece el rango de tensión del ADC entre 0 y 3.3V
y 12 bits para el rango de adquisición entre 0 y 4095
'''
pos_x.atten(ADC.ATTN_11DB)
pos_y.atten(ADC.ATTN_11DB)
pos_x.width(ADC.WIDTH_12BIT)
pos_y.width(ADC.WIDTH_12BIT)

'''
utiliza Read() para leer el valor de los ejes X e Y
y a continuación muéstralos en pantalla.
'''
# In the code, configure Z_Pin to pull-up input mode.
# In loop(), use Read () to read the value of axes X and Y 
# and use value() to read the value of axis Z, and then display them.
while True:
    print("X,Y:",pos_x.read(),",",pos_y.read())
    time.sleep(0.5)
