## <FONT COLOR=#007575>**13. Radar de marcha atrás**</font>
### <FONT COLOR=#AA0000>Resumen</font>
Cuando un coche se pone en marcha atrás, emite una señal acústica que indica que la distancia con los obstáculos situados detrás es inferior a un valor determinado, por ejemplo, en una plaza de aparcamiento. En este proyecto, hemos construido un radar de marcha atrás para coches con un sensor ultrasónico para la detección de distancias, un altavoz para emitir la señal acústica y un módulo de semáforo que hace las veces de indicador.

### <FONT COLOR=#AA0000>Ordinograma</font>

![13. Radar de marcha atrás](../img/MB/P13.png){.center-img}

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P13MP.py](../programas/MP/Proy/P13MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
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
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, cuando el valor de distancia detectado es superior a 40 cm, el LED verde se enciende y el amplificador no emite ningún sonido. Si el valor es inferior a 40 cm, el LED rojo se enciende y el amplificador emite un sonido de alarma.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
