## <FONT COLOR=#007575>**16. Telémetro ultrasónico**</font>
### <FONT COLOR=#AA0000>Resumen</font>
En este proyecto, combinamos el sensor ultrasónico y el módulo OLED para construir un medidor de distancia, cuyo alcance de detección está entre los 4 y los 300 cm.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P16MP.py](../programas/MP/Proy/P16MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P16MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
from machine import Pin,PWM
from oled import OLED
import time

# Inicializa interface I2C
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

oled = OLED(i2c)

# pines de control del sensor de ultrasonidos
Trigger = Pin(5, Pin.OUT) 
Echo = Pin(4, Pin.IN)

distancia = 0
VelocidadSonido = 340

def obtenDistancia():
    Trigger.value(1)
    time.sleep_us(10) #para habilitar el sensor de ultrasonidos
    Trigger.value(0)
    while Echo.value() == 0:
        Inicio = time.ticks_us()
    while Echo.value() == 1:
        Fin = time.ticks_us()
    Tiempo = time.ticks_diff(Fin,Inicio)
    distancia =  Tiempo * VelocidadSonido //2 // 10000
    return distancia

while True:
    distancia = obtenDistancia()
    oled.clear()
    oled.show_text("Distancia medida:", 0, 0)
    #Usa str() para convertir el valor de distancia en una cadena
    oled.show_text(str(distancia), 40, 20)
    oled.show_text("cm", 70, 20)
    oled.oled.show()
    time.sleep(1)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, verás que en la primera línea aparecerá "Distancia medida:". A continuación, en la segunda línea, se muestra el valor de la distancia en "cm".

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
