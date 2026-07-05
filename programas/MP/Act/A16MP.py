'''
 * Archivo         : A16MP
 * Versión Thonny  : Thonny 5.0.0
-----------------------------------------
oled.clear()
    borra la pantalla.
    Si quieres mostrar contenido nuevo, tienes que borrar el último que
    se ha mostrado; de lo contrario, ambos contenidos se superpondrán.

oled.oled.show()
    Actualiza la pantalla para ver el nuevo contenido en la pantalla OLED

oled.show_text("******", X,Y)
    Escribe el testo que se va a mostrar entre comillas dobles y establece
    los valores de X e Y para controlar la posición inicial de la visualización.
'''
import machine
from oled import OLED

# Inicializa el interface I2C
i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))

# crea objeto I2C
oled = OLED(i2c)

# borra la pantalla
oled.clear()

# muestra textos
oled.show_text("Coding Box", 20, 0)
oled.show_text("Hola Mundo!", 20, 20)
oled.show_text("MicroPython", 20, 40)

# mostrar
oled.oled.show()
