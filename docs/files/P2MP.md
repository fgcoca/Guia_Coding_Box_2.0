## <FONT COLOR=#007575>**2. Efecto breathing usando PWM**</font>
### <FONT COLOR=#AA0000>Resumen</font>
El LED con efecto respiración PWM utiliza un PWM programable integrado para generar una forma de onda analógica. Tras el encendido, el brillo del LED se puede ajustar mediante el ciclo de trabajo de dicha forma de onda, lo que permite crear el mencionado efecto. De este modo, se puede simular la luz ambiental modificando el brillo del LED con el paso del tiempo. Además, el LED con efecto de respiración puede crear un pequeño espectáculo de luces de colores que crea un ambiente tranquilo y acogedor.

En la actividad [14. Servomotor](https://fgcoca.github.io/Guia_Coding_Box_2.0/files/A14MP/#pwm) puedes encontrar la descripción completa del concepto de PWM.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P2MP.py](../programas/MP/Proy/P2MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P2MP
 * Versión Thonny  : Thonny 5.0.0
'''
from machine import Pin, PWM  
import time  
  
# Establece el pin y la frecuencia del PWM  
pwm_pin = Pin(23, Pin.OUT)  
pwm = PWM(pwm_pin, freq=1000)  # frecuencia de 1000Hz  
  
# parpadeo del LED  
while True:  
    for duty in range(0, 1024, 5):  # aumenta luminosidad gradualmente
        pwm.duty(duty)  
        time.sleep_ms(10)  # peuqeño retardo para observar mejor el efecto  
    for duty in range(1023, -1, -5):  # apagado gradual
        pwm.duty(duty)  
        time.sleep_ms(10)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, verás que el LED rojo se enciende y apaga gradualmente.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
