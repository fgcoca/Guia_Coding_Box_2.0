## <FONT COLOR=#007575>**11. Ventilador automático**</font>
### <FONT COLOR=#AA0000>Resumen</font>
Con la llegada del verano, las temperaturas van en aumento, por lo que algunos lugares públicos se equiparán con ventiladores automáticos que detectan la temperatura ambiente. Cuando la temperatura alcanza un valor predeterminado, el ventilador se enciende. Hemos añadido un sensor de movimiento PIR para reducir el consumo energético. Así, el ventilador solo se encenderá cuando se alcance esa temperatura y se detecte presencia.

### <FONT COLOR=#AA0000>Ordinograma</font>

![11. Ventilador automático](../img/MB/P11.png){.center-img}

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P11MP.py](../programas/MP/Proy/P11MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P11MP
 * Versión Thonny  : Thonny 5.0.0
'''
#importa I2C y Pin desde el módulo machine
from machine import I2C, Pin
#importa AHT20 desde la libreria aht20
from aht20 import AHT20
import time
#crea objeto I2C y los pines SDA y SCL
i2c = I2C(scl=Pin(22), sda=Pin(21))
#crea un objeto AHT20, inicializa el objeto I2C para comunicarse con el sensor
sensor = AHT20(i2c)

PIR = Pin(19,Pin.IN)
INB = Pin(18,Pin.OUT)
INA = Pin(17,Pin.OUT)

while True:	
    try:
        #almacena la temperatura y la humedad en las variables
        temperatura, humedad = sensor.read_temperature_humidity()
        pir = PIR.value()
        '''
        Determina si PIR detecta personas y la temperatura supera 25 grados.
        Si es cierto el ventilador gira y si no lo es permanece parado.
        '''
        if pir == 1 and temperatura > 25:
            INB.on()
            INA.off()
        else:
            INB.off()
            INA.off()
    #detecta y lee el sensor e imprime "Fallo de lectura del sensor:"
    #si hay un error de lectura.
    except RuntimeError as e:
        print("Fallo de lectura del sensor: ", e)
    time.sleep(1)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, cuando la temperatura supera el valor establecido y el sensor de movimiento PIR detecta a alguien, el ventilador se enciende. Si no se cumple alguna de estas dos condiciones, el ventilador no se pondrá en marcha.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
