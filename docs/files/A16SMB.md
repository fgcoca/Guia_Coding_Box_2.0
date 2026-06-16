## <FONT COLOR=#007575>**16. Pantalla OLED**</font>

!!! info ""
    !!! Note "Aviso importante"
        En el momento de la elaboración de este tutorial para Coding Box 2.0, no existe ningún bloque disponible en STEAMakersBlocks que permita la integración o el uso directo del sensor geomagnético I2C. Por este motivo, las funcionalidades relacionadas con este dispositivo no pueden implementarse mediante bloques estándar de STEAMakersBlocks para ESP32 y requerirían métodos alternativos de programación o futuras actualizaciones de la plataforma que incorporen soporte para este sensor.

En este caso, el dispositivo se comunica mediante el protocolo I²C y utiliza la dirección 0x3C. A priori, esto sugiere que el bloque "Iniciar I2C..." debería ser suficiente para llevar a cabo la configuración del periférico. Sin embargo, la biblioteca empleada por STEAMakersBlocks (Adafruit_SSD1306) no asigna las líneas de comunicación SDA y SCL conforme al conexionado implementado en la Coding Box 2.0, sino que invierte dicha correspondencia. Como consecuencia, la inicialización del controlador de la pantalla no se realiza correctamente y, al ejecutar el programa, el display presenta artefactos visuales o una imagen difusa ("niebla"), impidiendo su funcionamiento normal.

**¿Qué pasa si se intercambian los pines?**

* **Datos corrompidos**: La pantalla no recibe los comandos de inicialización correctos. El chip controlador (generalmente SSD1306) interpreta los pulsos de reloj como datos aleatorios.
* **Ruido visual**: Esto enciende píxeles al azar, creando un efecto de "niebla", "nieve" o líneas aleatorias.
* **Texto residual**: Se pueden mostrar caracteres extraños o palabras incompletas.
* **No hay daño permanente**: Por fortuna, intercambiar SDA y SCL no rompe la pantalla ni el microcontrolador. Solo impide que se comuniquen.
