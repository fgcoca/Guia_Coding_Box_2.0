## <FONT COLOR=#007575>**1. Parpadeo de un LED**</font>
### <FONT COLOR=#AA0000>Resumen</font>
Es uno de los proyectos de programación más sencillos para principiantes con la ESP32 Coding Box. Es el tipo de proyecto "Hola Mundo" típico de placas microcontroladas. Este sencillo proyecto ayuda a los principiantes a dominar mejor los conceptos básicos.

### <FONT COLOR=#AA0000>Esquema</font>
![Esquema interno LEDs](../img/MB/Esq1.png){.center-img33}

**LED activado**: la corriente de salida de los puertos de E/S está limitada, por lo que es posible que el brillo del LED no sea suficiente. Por este motivo, se añade al circuito un transistor NPN (Q1) que hace las veces de interruptor. Solo hay que aplicar un nivel alto (bajo) en la base del mismo para encenderlo (apagarlo).

Conducción/bloqueo del transistor: en pocas palabras, cuando la base recibe un nivel alto, el colector y el emisor se conectan, de modo que VCC pasa a través de la resistencia limitadora de corriente hacia el LED, luego al transistor y, por último, a tierra, formando un bucle. En ese momento, el LED está encendido. Cuando la base recibe un nivel bajo, colector y emisor se desconectan, por lo que no se puede formar el bucle de corriente y el LED se apaga.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el archivo original 3-1-led.py y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

Alternativamente puedes descargar el programa [A1MP.py](../programas/MP/Act/A1MP.py) modificado para este tutorial o bien copiar y pegar en el IDE de Thonny las siguientes líneas de código:

```python
'''
 * Archivo         : A1MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin # Importa la clase Pin para trabajar con GPIO
import time # Para funciones de retardo

led = Pin(23,Pin.OUT) 	# Establece IO23 como pin de control del LED rojo

#Bucle infinito, para que el código se pueda ejecutar repetidamente
while True:
    led.on()			#LED rojo encendido
    time.sleep(1)		#Retardo de 1 segundo
    led.off()			#LED rojo apagado
    time.sleep(1)		#Retardo de 1 segundo
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Una vez cargado el código, el LED rojo parpadeará con un intervalo de 1 segundo.

Si quieres que el LED parpadee con más frecuencia, solo tienes que cambiar el tiempo de retardo a 200 ms por ejemplo. Para ello la línea ```time.sleep(1)``` debes cambiarla por ```time.sleep_ms(200)```.
