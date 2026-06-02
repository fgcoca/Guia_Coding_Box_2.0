El microcontrolador ESP32 tiene una arquitectura de pines sumamente flexible pero con restricciones importantes que debes conocer para evitar bloqueos en el arranque o daños en el hardware.

## <FONT COLOR=#007575>**Clasificación por Funcionalidad Principal**</font>
Aunque la mayoría son **GPIO** (Entrada/Salida de Propósito General), se dividen en grupos con capacidades únicas:

* **Pines de Entrada y Salida (Bidireccionales):** Son la mayoría y pueden leer o enviar señales digitales.
* **Pines Solo de Entrada (GPI):** Los GPIO 34, 35, 36 y 39 no tienen capacidad de salida. No puedes usarlos para encender un LED o activar un relé. Además, **no tienen resistencias pull-up/down internas**.
* **Pines de Arranque (Strapping Pins):** Los GPIO 0, 2, 5, 12 y 15 determinan cómo arranca el chip. Si se conecta algo que los fuerce a un estado incorrecto al encender (por ejemplo, un pulsador a GND en el GPIO 0), el ESP32 podría entrar en "modo carga de firmware" y no ejecutar código.
* **Pines de la Flash Interna:** Los GPIO 6 al 11 están conectados internamente a la memoria Flash. No se deben usar en proyectos o el sistema colapsará inmediatamente.

## <FONT COLOR=#007575>**Capacidades Especiales (Multiplexación)**</font>
Gracias a una matriz de IO, casi cualquier pin puede realizar funciones avanzadas:

* **PWM:** Hasta 16 canales independientes para controlar brillo de LEDs o motores en cualquier pin de salida.
* **Touch (Sensores Táctiles):** 10 pines (como GPIO 0, 2, 4, 12-15, 27, 32, 33) pueden detectar el ser tocados con la mano.
* **RTC (Real Time Clock):** Los pines marcados como RTC (como los 34-39 y otros) siguen funcionando cuando el ESP32 está en Deep Sleep, permitiendo despertar al chip con sensores externos.
* **Pines recomendados para uso libre:** GPIO 13, 14, 16, 17, 18, 19, 21, 22, 23, 25, 26, 27, 32 y 33.

## <FONT COLOR=#007575>**Pines analógicos**</font>
El ESP32 cuenta con hasta 18 canales de ADC (convertidor analógico-digital) de 12 bits (2^12 = 4096) distribuidos en GPIOs 32-39 (ADC1) y 0, 2, 4, 12-15, 25-27 (ADC2), funcionando a 3.3V. Permiten leer sensores analógicos y potenciómetros con precisión.

!!! Note "Nota:"
    **ADC2 no funciona cuando se usa WiFi.**

### <FONT COLOR=#AA0000>Características Principales de los Pines Analógicos</font>
* **Resolución**: 12 bits por defecto (2^12 = 4096), aunque ajustable a 10 bits (2^10 = 1024) o menos.
* **Voltaje Máximo**: 3.3V. Importante: No son tolerables los 5V; aplicar más de 3.6V puede dañar el ADC.
* **Canales ADC1 (8 pines)**: GPIO 32, 33, 34, 35, 36, 37, 38, 39.
* **Canales ADC2 (10 pines)**: GPIO 0, 2, 4, 12, 13, 14, 15, 25, 26, 27.
* **Salidas Analógicas (DAC)**: El ESP32 tiene 2 convertidores digital-analógico (DAC) de 8 bits reales en los pines GPIO 25 y GPIO 26 (0 a 255 para 0 a 3.3V).

### <FONT COLOR=#AA0000>Consideraciones al usar ADC</font>
* **WiFi y ADC2:** Cuando se utiliza la conexión **WiFi**, el **ADC2** **NO** está **disponible** para su uso. Se recomienda usar ADC1 para lecturas analógicas continuas.
* **Linealidad:** La respuesta del ADC del ESP32 no es completamente lineal, especialmente cerca de 0V y 3.3V.
* **Pines de entrada solamente:** Los GPIOs 34 al 39 no tienen resistencias pull-up/pull-down internas y son solo para entrada.

### <FONT COLOR=#AA0000>Consideraciones PWM</font>
El ESP32 es extremadamente versátil y permite configurar casi cualquier pin GPIO como salida PWM (Modulación por Ancho de Pulso) utilizando su controlador LED PWM que cuenta con 16 canales independientes que pueden configurarse para generar señales PWM.

Los pines recomendados o seguros son los siguientes:

* {--GPIO2--}
* **GPIO4 - Echo ultrasonidos**
* **GPIO5 - Trigger ultrasonidos**
* {--GPIO12--}
* {--GPIO13--}
* {--GPIO14--}
* {--GPIO15--}
* **GPIO16 - LEDs RGB direccionables**
* **GPIO17 - Motor DC**
* **GPIO18 - Motor DC**
* **GPIO19 - Sensor de movimiento PIR**
* {--GPIO21--}
* {--GPIO22--}
* **GPIO23 - LED rojo**
* **GPIO25 - Servomotor**
* **GPIO26 - LED amarillo**
* **GPIO27 - LED verde**
* **GPIO32 - Altavoz**
* **GPIO33 - ADKey**

Los pines GPIO34, GPIO35 (Joystick), GPIO36 (LDR) y GPIO39 (Joystick) son solo de entrada y no pueden generar señales PWM por lo que se deben evitar para este uso.
