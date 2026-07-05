## <FONT COLOR=#007575>**12. Monitorización del entorno**</font>
### <FONT COLOR=#AA0000>Resumen</font>
En este proyecto, utilizamos la pantalla OLED para mostrar los valores de temperatura, humedad, presión atmosférica y altitud del entorno en que tenemos situada nuestra Coding Box. Podría considerarse que se trata de un sencillo dispositivo de monitorización ambiental.

### <FONT COLOR=#AA0000>Prueba del código</font>
Abre Thonny. Conecta la placa al ordenador y selecciona el puerto al que está conectada Coding Box. En "Archivos", abre el programa [P12MP.py](../programas/MP/Proy/P12MP.py) y haz clic en el botón ![Botón ejecutar](../img/Pyth/run.png).

El programa es:

```python
'''
 * Archivo         : P12MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
#importa I2C y Pin desde el módulo machine
from machine import I2C, Pin
#importa AHT20 desde la libreria aht20
from aht20 import AHT20
#importa BMP388 desde la libreria BMP388
from bmp388 import BMP388
from oled import OLED
import time

#crea objeto I2C y los pines SDA y SCL
i2c = I2C(scl=Pin(22), sda=Pin(21))
#crea un objeto AHT20, inicializa el objeto I2C para comunicarse con el sensor
sensor = AHT20(i2c)

#crea un objeto BMP388 y establece los pines SCL y SDA, establece la frecuencia en 100KHz
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21), freq=100000)

#crea un objeto BMP388, inicializa el objeto I2C para comunicarse con el sensor
bmp = BMP388(i2c, i2c_addr=0x76)

# crea ejemplo OLED
oled = OLED(i2c)
# borra oled
oled.clear()

'''
La función str() convierte una variable de tipo cadena a partir de una variable
de otro tipo. 

La función int() convierte una variable de otro tipo a una variable de tipo
entero. El motivo de esta conversión es que no se muestran los datos tras la
conversión de la unidad de presión decimal: 1 hPa = 1 × 100 Pa = 100 Pa
'''

while True:
    try:
        #almacena la temperatura y la humedad en las variables
        temperatura, humedad = sensor.read_temperature_humidity()
        # lee la presión.
        presion = bmp.read_pressure() // 100 #Convierte Pa a hPa dividiendo la presion entre 100        
        # borra pantalla
        oled.clear()
        # muestra la presión
        oled.show_text("Presion:", 0, 0)
        oled.show_text(str(int(presion)), 70, 0)
        oled.show_text("hPa", 105, 0)
        # muestra la temperatura
        oled.show_text("Temperatura:", 0, 15)
        oled.show_text(str(int(temperatura)), 100, 15)
        oled.show_text("C", 120, 15)
        # muestra la humedad
        oled.show_text("Humedad:", 0, 30)
        oled.show_text(str(int(humedad)), 75, 30)
        oled.show_text("%", 105, 30)

        # muestra oled
        oled.oled.show()
    # detect and read value, print “Failed to read from sensor:” if an error occurs
    except RuntimeError as e:
        print("Fallo de lectura del sensor: ", e)
    time.sleep(1)
```

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Haz clic en "Ejecutar script actual" ![Botón ejecutar](../img/Pyth/run.png) para ejecutar el código. Tras cargar el código, en la pantalla OLED podrás ver los valores de temperatura, humedad y presión atmosférica. Estos valores se actualizan cada tres segundos.

Pulsa "Ctrl+C" o haz clic en "Detener/Reiniciar el intérprete" ![Icono](../img/Pyth/I_stop.png) para detener la ejecución.
