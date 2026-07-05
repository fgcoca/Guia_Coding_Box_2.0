'''
 * Archivo         : A15_amp_MP.py
 * Versión Thonny  : Thonny 5.0.0
------------------------------------------

 ~ Programa para iluminar en rojo, verde y azul los LEDs del anillo de manera progresiva
 ~ Después del color azul se apagan todos también de manera progesiva y permanecen así 3s
 
    color = [rojo,verde,azul]
    color almacena el valor de los colores.
    rojo,verde,azul coresponde a valores RGB en el rango 0-255
    rojo [255,0,0]
    establece el color que deseas mostrar según la tabla de colores RGB
'''
#importa módulos necesarios: Pin, neopiexl y time.
from machine import Pin
import neopixel
import time

pin = Pin(16, Pin.OUT) #define el pin de control SK6812 como IO16
num_pixels = 12 #establece el número de LEDs SK6812 en 12
#inicializa SK6812
np = neopixel.NeoPixel(pin, num_pixels)
rojo = [255,0,0] #rojo
verde = [0,255,0] #verde
azul = [0,0,255] #azul

while True:
    for i in range(num_pixels): #bucle for: i varia de 0 a 11
        np[i] = rojo #mostrar rojo en i
        np.write() #muestra el color
        time.sleep_ms(50) #retardo de 50ms para cambiar el color gradualmente
    time.sleep(1) #Pausa de 1 segundo despues de mostrar
    for i in range(num_pixels):
        np[i] = verde #mostrar verde en i
        np.write()
        time.sleep_ms(50)
    time.sleep(1)
    for i in range(num_pixels):	
        np[i] = azul #azul
        np.write()
        time.sleep_ms(50)
    time.sleep(1)
    for i in range(num_pixels):	
        np[i] = [0,0,0] #negro o apagar LEDs
        np.write()
        time.sleep_ms(50)
    time.sleep(3) #permanecen apagados 3 segundos

