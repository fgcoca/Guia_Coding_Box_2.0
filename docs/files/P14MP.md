## <FONT COLOR=#007575>**14. Reloj RGB**</font>
### <FONT COLOR=#AA0000>Resumen</font>
En este proyecto, hemos construido un reloj con el anillo RGB, en el que utilizamos tres colores que representan la hora, los minutos y los segundos, respectivamente (rojo, verde y azul). Dado que el anillo solo tiene 12 LED, cada uno equivale a 5 segundos o minutos (60/12 = 5).

### <FONT COLOR=#AA0000>Ordinograma</font>
Como se muestra en el diagrama de flujo, utilizamos el rojo para las horas, el verde para los minutos y el azul para los segundos. Cuando el segundo alcanza el valor 60, el minuto se incrementa en 1, y cuando el minuto alcanza el valor 60, la hora se incrementa en 1.

???+ Tip "Aviso:"
    Adoptamos 60/5 = 12 en lugar de 59/5 = 11,8, ya que el tipo de variable es entero y el valor debe dividirse por 5. Además, 60 se puede dividir perfectamente en 12 partes.

![14. Reloj RGB](../img/MB/P14.png){.center-img}

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P14MP.py](../programas/MP/Proy/P14MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
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
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, verás que el anillo RGB muestra la hora a partir del valor establecido en los bloques iniciales: rojo para la hora, verde para los minutos y azul para los segundos. Cada minuto, el color azul da una vuelta completa. Solo se mostrará un color cuando se superpongan. El azul no cubrirá el verde ni el verde cubrirá el rojo.

???+ Failure "Ten en cuenta que"
    se trata de un reloj peculiar en el que el error se va acumulando con el tiempo.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
