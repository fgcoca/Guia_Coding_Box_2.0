## <FONT COLOR=#007575>**3. Control de LED con botón**</font>
### <FONT COLOR=#AA0000>Resumen</font>
En este proyecto, controlamos el encendido y apagado del LED mediante un botón ADKey. El LED se enciende al pulsar el botón y se apaga al volver a pulsarlo.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P3MP.py](../programas/MP/Proy/P3MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P3MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin,ADC
import time

led = Pin(23,Pin.OUT)
ADkey = ADC(Pin(33))			#establece el pin GPIO 33 como entrada ADC
ADkey.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
ADkey.width(ADC.WIDTH_12BIT)	#resolución del ADC
#define una variable para cambiar el estado del LED
estadoLED = False

while True:
    ValorADkey = ADkey.read()	#lee el valor analogico del boton
    if ValorADkey > 3500:	#si esmayor de 3500 indica que el botón se ha pulsado
        #Invierte el valor de estadoLED:
        #si es False pasa a ser True
        #si es True pasa a ser False.
        estadoLED = not estadoLED #invierte el estado del LED
        time.sleep_ms(500)
    #led.value() es diferente de led.on() / led.off(), ya que en led.value()
    #hay que introducir 0 (LED apagado) o 1 (LED encendido).
    led.value(estadoLED)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, pulsa el botón rojo y se encenderá el LED rojo; vuelve a pulsarlo y el LED se apagará.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.

Puedes probar el mismo programa con los botones y LEDs amarillo y verde.
