'''
 * Archivo         : P13MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,PWM
import time

#salida PWM pin: IO32, frecuencia: 5000 Hz, duty cycle: 50%
#El valor medio para resolución de 8 bit es 128, y el rango de duty cycle es 0-255)
altavoz = PWM(Pin(32), freq=5000, duty=128)
LEDrojo = Pin(23,Pin.OUT)
LEDverde = Pin(27,Pin.OUT)

# Pines de control sensor ultrasonidos
Trigger = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distancia = 0
VelocidadSonido = 340

# Función para calcular la distancia con el sensor de ultrasonidos
def obtenDistancia():
    Trigger.value(1)
    time.sleep_us(10) #para habilitar el sensor
    Trigger.value(0)
    #Inicio es el tiempo de la señal en el aire
    while Echo.value() == 0:
        Inicio = time.ticks_us()
    #Fin es el tiempo cuando se recibe el rebote
    while Echo.value() == 1:
        Fin = time.ticks_us()
    #Tiempo es la diferencia entre los anteriores
    Tiempo = time.ticks_diff(Fin,Inicio)
    #Calculo de la distancia
    distancia =  Tiempo * VelocidadSonido //2 // 10000
    #devuelve el valor calculado
    return distancia

while True:    
    distancia = obtenDistancia()
    print('Distancia: ',distancia, 'cm')
    if distancia > 40:
        LEDrojo.off()
        LEDverde.on()
        altavoz.duty(0)
    else:
        LEDrojo.on()
        LEDverde.off()
        altavoz.duty(50)
        altavoz.freq(880)
    time.sleep_ms(300)

