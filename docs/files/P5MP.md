## <FONT COLOR=#007575>**5. Cerrar ventana al oscurecer**</font>
### <FONT COLOR=#AA0000>Resumen</font>
En este proyecto, se programa el sistema para que la ventana se cierre automáticamente al anochecer. Para ello, necesitamos una fotorresistencia que detecte la luz ambiental. Establecemos un umbral para la fotorresistencia. Cuando el valor de la luz ambiental es inferior al umbral establecido, el servo cierra la ventana.

### <FONT COLOR=#AA0000>Ordinograma</font>

![5. Cerrar ventana al oscurecer](../img/MB/P5.png){.center-img}

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P5MP.py](../programas/MP/Proy/P5MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P5MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import ADC,Pin
import time
#importa Servo de la libreria servo
from servo import Servo

servo = Servo(pin=25)  #pin de control IO25

adc=ADC(Pin(36))			#entrada ADC pin GPIO 36
adc.atten(ADC.ATTN_11DB)	#rango de tensión 0-3.3V
adc.width(ADC.WIDTH_12BIT)	#resolución ADC

while True:
    luminosidad = adc.read()
    if luminosidad < 500:	#determina si la luminosidad es menor de 500
        servo.set_angle(180)  # gira un ángulo de 180 grados
    else:
        servo.set_angle(0)  # gira un ángulo de 0 grados
    time.sleep_ms(300)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, tapa la fotorresistencia para que su valor analógico sea inferior a 500 y el servo girará hasta los 180°. Si el valor analógico supera los 500, el servo girará hasta los 0°.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
