## <FONT COLOR=#007575>**6. Botones ADKey**</font>
### <FONT COLOR=#AA0000>Resumen</font>
Los botones ADKey solo necesitan un pin analógico para leer el estado de los botones, por lo que se ahorran puertos de E/S. Utilizan entrada analógica y los voltajes de salida varían en función del botón pulsado, por lo que se pueden obtener diferentes valores analógicos. A partir de estos valores, podemos determinar qué botón se ha pulsado.

### <FONT COLOR=#AA0000>Esquema</font>

![ADKey](../img/MB/ADKey.png){.center-img75}

Del esquema podemos deducir:

* Cuando no se presiona ningún botón la señal en el pin IO33 es la caida de tensión en la resistencia de 2K que está conectada a GND. Por lo tanto el valor analógico de IO33 es cero, es decir, nivel bajo o 0V.
* Cuando se presiona S1 (botón rojo), el pin IO33 se conecta directamente a 3.3V. Entonces el valor analógico en IO33 será 4095 (1023 en MicroBlocks), lo que equivale a 3.3V.
* Cuando se presiona S2 (botón amarillo), el pin IO33 tendrá como tensión la diferencia de potencial en la resistencia de 2K pero esta vez conectada a 3.3V mediante la resistencia de 1K. El valor analógico será de aproximadamente 2400 (650 en MicroBlocks) y la tensión será de $\frac{3.3\times2}{2+1}=2.2V$.
* Cuando se presiona S3 (botón verde), el pin IO33 tendrá como tensión la diferencia de potencial en la resistencia de 2K pero esta vez conectada a 3.3V mediante la resistencia de 1K en serie con la de 2K7. El valor analógico será de aproximadamente 1200 (320 en MicroBlocks) y la tensión será de $\frac{3.3\times2}{2+2.7+1}=1.16V$.

Un sencillo programa como el siguiente nos permite comprobar los valores en el pin IO33 según el botón pulsado:

![Valor analógico IO33](../img/MB/analogio33.png){.center-img}

### <FONT COLOR=#AA0000>Bloques</font>

==**De la clase Coding Box:**==

El bloque "cb ADKey ¿botón...presionado?" lee el valor analógico del módulo y determina que botón se ha pulsado de acuerdo con ese valor.

![Bloque](../img/MB/cb_ADKey.png){.center-img33}

Haz clic en el botón ![Desplegar menu](../img/MB/B_cb_flecha_abajo.png) para cambiar el botón:

![Bloque](../img/MB/cb_ADKey_op.png){.center-img33}

### <FONT COLOR=#AA0000>Prueba del código</font>
Puedes crear los bloques manualmente o abrir directamente el archivo de código que te puedes descargar del enlace: [6. Botones ADKey](../programas/MB/6_Botones_ADKey.ubp).

El programa es el siguiente:

<center>

![6. Botones ADKey](../img/MB/6_Botones_ADKey.png)  
***[6. Botones ADKey](../programas/MB/6_Botones_ADKey.ubp)***

</center>

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Conecta Coding Box a MicroBlocks mediante USB o Bluetooth y haz clic en el botón "ejecutar" para cargar el código en la misma. Si pulsas el botón rojo, se oye "Pulsaste el botón rojo"; si pulsas el botón amarillo, se oye "Pulsaste el botón amarillo"; si pulsas el botón verde, se oye "Pulsaste el botón verde".

![Resultado 6. Botones ADKey](../img/MB/R6_Botones_ADKeyR.png){.center-img75}

![Resultado 6. Botones ADKey](../img/MB/R6_Botones_ADKeyA.png){.center-img75}

![Resultado 6. Botones ADKey](../img/MB/R6_Botones_ADKeyV.png){.center-img75}
