## <FONT COLOR=#007575>**13. Motor DC (ventilador)**</font>
### <FONT COLOR=#AA0000>Resumen</font>
El motor de corriente continua está controlado por el chip HR1124S, un controlador de puente en H de un solo canal utilizado en motores de este tipo. Este utiliza transistores de potencia PMOS y NMOS con baja resistencia en estado activo, lo que garantiza una menor pérdida de potencia y un mayor tiempo de funcionamiento seguro.

El motor está conectado como vemos en la imagen siguiente:

![Esquema](../img/MB/motorDC.png){.center-img75}

El control del motor se realiza siguiendo la tabla lógica:

<center>

|IO17|IO18|Estado del motor|
|:-:|:-:|---|
|Alto (H)|Bajo (L)|Gira hacia delante|
|Bajo (L)|Alto (H)|Gira en sentido contrario|
|Alto (H)|Alto (H)|parada (una parada gradual)|
|Bajo (L)|Bajo (L)|freno (freno a tope)|

</center>

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [A13MP.py](../programas/MP/Act/A13MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : A13MP
 * Versión Thonny  : Thonny 5.0.0
------------------------------------------------------
Tabla lógica de giro del motor:
------------------------------------------------------
  IO17(INA) | IO18(INB)  | estado del motor          |
------------------------------------------------------ 
   Alto (H) |  Bajo (L)  | Gira en sentido contrario |
------------------------------------------------------
   Bajo (L) |  Alto (H)  | Gira en hacia delante     |
------------------------------------------------------
  Alto (H)  |  Alto (H)  | parada gradual            |
------------------------------------------------------
   Bajo (L) |  Bajo (L)  | freno a tope              |
------------------------------------------------------
'''

from machine import Pin
import time

#pin de control INA es IO17
INA = Pin(17,Pin.OUT)
#pin de control INB es IO18
INB = Pin(18,Pin.OUT)

while True:
    #adelante
    INA.off()
    INB.on()
    time.sleep(2)
    #atras
    INA.on()
    INB.off()
    time.sleep(2)
    #parar
    INA.off()
    INB.off()
    time.sleep(2)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Una vez cargado el código, verás que el ventilador gira en sentido horario durante 2s y, a continuación, gira en sentido antihorario durante otros 2s. Después se detiene. Estas acciones se repiten.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
