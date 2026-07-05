## <FONT COLOR=#007575>**15. LED RGB WS2812**</font>
### <FONT COLOR=#AA0000>Resumen</font>
El LED RGB WS2812 es un LED RGB de control externo que integra un circuito de control y un circuito emisor de luz. Utiliza un sistema de comunicación por código de retorno a cero de una sola línea y admite 256 niveles de gris para mostrar una gama completa de colores. El chip integrado en cada píxel estabiliza eficazmente la salida de color.Se utiliza ampliamente en iluminación, pantallas y decoración.

### <FONT COLOR=#AA0000>Esquema</font>
Coding Box dispone de 12 WS2812 colocados en forma circular y conectados según el siguiente esquema:

![Esquema](../img/MB/Esquema_WS2812.png){.center-img100}

Según el esquema, el WS2812 se conecta y transmite datos a través de un solo cable mediante el método de comunicación denominado "código de retorno a cero en bus único" (single NZR). Los datos se introducen en serie a través del pin DIN y cada píxel recibe y procesa 24 bits de datos (canales de color rojo, verde y azul, con 8 bits cada uno).

Para obtener información detallada sobre el modo de transmisión, consulta: [LED RGB direccionable](https://fgcoca.github.io/tiras-y-matrices-de-LEDs/#led-rgb-direccionable), donde podrás encontrar las especificaciones del WS2812.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [A15MP.py](../programas/MP/Act/A15MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : A15MP
 * Versión Thonny  : Thonny 5.0.0
'''
#Importa módulos necesarios: Pin, neopiexl y time.
from machine import Pin
import neopixel
import time

pin = Pin(16, Pin.OUT) #define el pin de control SK6812 como IO16
num_pixels = 12	#Establece el número de LEDs SK6812 en 12
#inicializa SK6812
np = neopixel.NeoPixel(pin, num_pixels)

rojo = [255,0,0] #establece el color en rojo

while True:
    np[10] = rojo #el primer LED se ilumina en rojo. 12 LEDS: números del 0 al 11
    np.write() #muestra el color en el LED
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, el primer LED del módulo WS2812 se iluminará en rojo.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.

### <FONT COLOR=#AA0000>Ampliación</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [A15_amp_MP.py](../programas/MP/Act/A15_amp_MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
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
```
