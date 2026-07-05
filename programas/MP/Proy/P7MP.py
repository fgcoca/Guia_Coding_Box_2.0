'''
 * Archivo         : P7MP
 * Versión Thonny  : Thonny 5.0.0
'''

from machine import Pin, PWM
import time

#Establece el pin, la frecuencia y el ciclo de trabajo del 0% del PWM
trompeta = PWM(Pin(32), freq=5000, duty=0)

# define una matriz para almacenar las frecuencias
a = [523, 587, 659, 698, 784, 880, 988]

# establece los pines de control del sensor ultrasónico
Trigger = Pin(5, Pin.OUT)
Echo = Pin(4, Pin.IN)

distancia = 0  # valor inicial de la distancia
VelocidadSonido = 340  # 340 m/s

def obtenerDistancia():
    """
    habilita el sensor de ultrasonidos para detectar la distancia
    retorna la distancia detectada en cm
    """
    # mantiene el Trigger en alto 10 us para habilitar el sensor
    Trigger.value(1)
    time.sleep_us(10)
    Trigger.value(0)
    
    #espera hasta que el pin Echo está em estado alto. Almacena el timepo de inicio
    while Echo.value() == 0:
        Inicio = time.ticks_us()
        
    #espera hasta que el pin Echo está em estado bajo. Almacena el timepo de finalización
    while Echo.value() == 1:
        Paro = time.ticks_us()
    
    # calcula el tiempo que el pin Echo está en estado alto
    Tiempo = time.ticks_diff(Paro, Inicio)
    # calcula la distancia en cm
    ValorDistancia = Tiempo * VelocidadSonido // 2 // 10000 #// = división entera
    return ValorDistancia

def toca_nota(index):
    # Reproduce la escala especificada
    trompeta.duty(40)  #el duty cycle（0-255）del PWM ajusta el volumen del sonido
    trompeta.freq(a[index])  #frecuencia PWM corresponde a la frecuencia del tono
    time.sleep_ms(500)  #reproduce el tono durante 500ms
    trompeta.duty(0)  #detiene el tono 

while True:
    distancia = obtenerDistancia()  #obtener el valor de la distancia
    # reproduce el tono de acurdo con la distancia detectada
    if 5 < distancia < 10:
        print("Do")
        toca_nota(0)
    elif 10 < distancia < 15:
        print("Re")
        toca_nota(1)
    elif 15 < distancia < 20:
        print("Mi")
        toca_nota(2)
    elif 20 < distancia < 25:
        print("Fa")
        toca_nota(3)
    elif 25 < distancia < 30:
        print("So")
        toca_nota(4)
    elif 30 < distancia < 35:
        print("La")
        toca_nota(5)
    elif 35 < distancia < 40:
        print("Si")
        toca_nota(6)
    
    time.sleep_ms(100)  # retardo entre medidas

