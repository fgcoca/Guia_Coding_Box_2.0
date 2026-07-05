'''
 * Archivo         : A7MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,PWM
import time

# define los pines de control del sensor de ultrasonidos
Trig = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distancia = 0 # inicializa la variable distancia a 0
VelocidadSonido = 343 #A 20ºC es de 343,2 m/s

'''
La función obtenerDistancia() mide la distancia, mientras que Echo.value()
lee el estado del pin de Echo. Utiliza la función timestamp del módulo time
para calcular la duración del nivel alto del pin Echo, calcula la distancia
medida en función de ese tiempo y devuelve el valor.
'''

def obtenerDistancia():
    # Habilitar sensor. Trig a nivel alto 10 µs
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    #empezar a contar, en el momento inicial de la propagación de la onda ultrasónica en el aire
    while Echo.value() == 0:
        Iniciar = time.ticks_us()
    #El momento en que se recibe el rebote de la onda ultrasónica reflejada
    while Echo.value() == 1:
        Parar = time.ticks_us()
    #El tiempo de recepción menos el tiempo inicial es el tiempo total.
    Tiempo = time.ticks_diff(Parar,Iniciar)
    #Calcula la distancia en metros
    #Divide por 10000 para convertir a centímetros
    distancia =  Tiempo * VelocidadSonido //2 // 10000
    #Retorna el resultado calculado
    return distancia

# Muestra el valor medido cada 500ms
while True:    
    print('Distancia medida: ', obtenerDistancia(), 'cm')
    time.sleep_ms(500)