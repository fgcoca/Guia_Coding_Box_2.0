'''
 * Archivo         : P14MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin
import neopixel
import time  
  
hora = 10 	#horas
minuto = 30 #minutos
segundo = 40	#segundos

pin = Pin(16, Pin.OUT)	#pin de control IO16 de SK6812 
num_leds = 12			#número de LEDs
#inicializa SK6812
led = neopixel.NeoPixel(pin, num_leds)

rojo = [255,0,0]	#rojo-hora
verde = [0,255,0]#verde-minuto
azul = [0,0,255]	#azul-segundo
  
def setClock():
    # Usa la variable global para modificar las variables
    global hora, minuto, segundo 
    segundo += 1  
    if segundo > 59:  
        segundo = 0  
        minuto += 1  
        if minuto > 59:  
            minuto = 0  
            hour += 1  
            if hora > 12:  
                hora = 1  
    # Imprime formateado la hora actual 
    print(f"{hora:02d}:{minuto:02d}:{segundo:02d}")  
    time.sleep(1)  
  
while True:  
    setClock() 
    if segundo // 5 == 0:
        for i in range(0,11):	#limpia segundos
            np[i] = 0,0,0
        led[11] = azul
        led.write()		#actualiza los LEDs
    else:
        led[int(segundo // 5 - 1)] = azul
        led.write()		#actualiza los LEDs
    if minuto // 5 == 0:
        led[11] = verde
        led.write()		#actualiza los LEDs
    else:
        led[int(minuto // 5 - 1)] = verde
        led.write()		#actualiza los LEDs
    led[(hora-1)] = rojo
    led.write()		#actualiza los LEDs
