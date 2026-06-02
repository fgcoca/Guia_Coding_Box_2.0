## <FONT COLOR=#007575>**14. Servomotor**</font>
### <FONT COLOR=#AA0000>El servo</font>
Un servomotor o abreviado servo es un motor especial que puede posicionar su eje en un ángulo determinado y lo puede mantener en esta posición. Los servos estándar suelen girar 180º, pero es habitual encontrar servos que giran 90º y otros 360º, que son los conocidos como servos de rotación continua. En el interior del mismo están ubicados tanto la electrónica de control como los engranajes reductores que a su vez pueden llevar o no topes físicos que marquen el ángulo de giro. Para su funcionamiento sólo necesitan ser alimentados (conexiones GND y VCC o 5V) y una señal de control.

Los servomotores son en realidad motores de corriente continua a los que se les ha añadido una reductora, para que giren más despacio y con más fuerza, y un controlador electrónico que permite hacer que gire un determinado ángulo. Además, el servo en todo momento sabe en qué posición está, aunque se apague o reinicie. Esto significa que si a un servo que hemos movido a un determinado punto, lo hemos dejado sin alimentación y al alimentarlo de nuevo le indicamos que gire 90º, no va a girar 90º sino que se va a dirigir a su posición de 90º que tiene memorizada internamente.

En la figura siguiente vemos el interior de un servo esquematizado.

![Esquema interior servo](../img/MB/esq_servo.png){.center-img100}

Su aspecto real lo vemos en esta otra figura, donde también se aprecian los accesorios y tornillería que lo acompañan.

![Aspecto real servo](../img/MB/aspecto.png){.center-img}

Veamos su principio básico de funcionamiento: La electrónica de control del servomotor tiene un circuito de referencia incorporado que emite la señal de referencia, que es un ciclo de 20 ms con un ancho de pulso de 1,5 ms. Se compara la tensión de control recibida con la de referencia y se genera una diferencia de tensión. El circuito de control en la placa decidirá la dirección de rotación en consecuencia y accionará el motor. El sistema de engranajes o reductora convierten el giro del motor en un par de fuerza a través del eje. El sensor detecta que se ha alcanzado la posición enviada de acuerdo con la señal de retroalimentación. Cuando la diferencia de tensión existe el motor gira y cuando la diferencia se reduce a cero, el motor se detiene. Normalmente, el ángulo de rotación es de 0 a 180 grados.

El servomotor viene con un conector hembra de tres pines para tres cables de conexión, que se distinguen por los colores marrón, rojo y naranja (diferentes marcas pueden tener diferentes colores).

El ángulo de rotación del servomotor se controla regulando el ciclo de trabajo de la señal PWM cuyo estándar es de 20 ms (50 Hz).

El ángulo de rotación del servo se controla ajustando el ciclo de trabajo de las señales PWM (modulación por ancho de pulso). En teoría, el período de la señal PWM estándar es fijo, de 20 ms (50 Hz), por lo que el ancho del pulso debería ser de 1 a 2 ms. Sin embargo, en la práctica, este periodo oscila entre 0,5 ms y 2,5 ms, lo que corresponde a un ángulo del servo de 0° a 180°.

### <FONT COLOR=#AA0000>PWM</font>
PWM son siglas en inglés que significan Pulse Width Modulation y que lo podemos traducir a español como Modulación de ancho de pulso. Los pines PWM permiten generar una señal analógica mediante una salida digital mapeada con 8 bits, o lo que es lo mismo, valores del 0 al 255, es decir mediante una salida PWM podemos emular una señal analógica.

En realidad una placa tipo UNO no es capaz de generar una salida analógica y lo que se hace es emplear un truco que consiste en activar una salida digital durante un tiempo y el resto del tiempo del ciclo mantenerla desactivada. El valor promedio de la salida es el valor analógico. En el tipo de modulación PWM mantendremos constante la frecuencia, o lo que es lo mismo, el tiempo entre pulsos y lo que se hace es variar la anchura del pulso.

La proporción de tiempo que está encendida la señal, respecto al total del ciclo, se denomina ciclo de trabajo o Duty cycle, y generalmente se expresa en tanto por ciento. En la imagen siguiente vemos señales con distintos ciclos de trabajo.

![Distintos Duty cicle](../img/MB/Duty.png){.center-img100}

Es importante recordar que en una salida PWM el valor de la tensión es 5V por lo que si alimentamos un dispositivo de 3V a partir de una salida de 5V lo dañaremos de forma irreversible.

La señal PWM emula una señal analógica para aplicaciones como variar la luminosidad de un LED y variar la velocidad de motores de corriente continua.

En la Coding Box se utilizan muchos pines con PWM y los del motor están entre ellos.

### <FONT COLOR=#AA0000>Bloques</font>

==**De la clase Coding Box:**==

El bloque "cb pon el servo a..." controla el ángulo de rotación del servomotor.

![Bloque](../img/MB/cb_pon_servo.png){.center-img}

### <FONT COLOR=#AA0000>Prueba del código</font>
Puedes crear los bloques manualmente o abrir directamente el archivo de código que te puedes descargar del enlace: [14. Servomotor](../programas/MB/14_servo.ubp).

El programa es el siguiente:

<center>

![14. Servomotor](../img/MB/14_servo.png)  
***[14. Servomotor](../programas/MB/14_servo.ubp)***

</center>

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Conecta Coding Box a MicroBlocks mediante USB o Bluetooth y haz clic en el botón "ejecutar" para cargar el código en la misma. El servo gira hasta los 0° y permanece así durante 2 segundos (si su ángulo inicial es 0°, no girará); a continuación, gira hasta los 90° y permanece así durante 2 segundos. Por último, gira hasta los 180 grados y permanece así durante dos segundos. Este proceso se ejecuta si el bloque "si" tiene el interruptor en verde. En caso de estar en rojo no se ejecuta esta parte del código. El servo gira hasta los 0° y permanece así durante 1 segundo y va girando hasta los 180 grados a incrementos de 10 grados, pudiendo nosotros cambiar este incremento a voluntad.
