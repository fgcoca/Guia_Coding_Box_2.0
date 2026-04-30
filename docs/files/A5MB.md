## <FONT COLOR=#007575>**5. Fotoresistencia o LDR**</font>
### <FONT COLOR=#AA0000>Resumen</font>
Una fotorresistencia es un dispositivo fotoeléctrico que funciona basándose en la fotoconductividad de los semiconductores. Se puede utilizar para detectar la luminosidad del entorno actual y generar el valor analógico correspondiente.

La fotorresistencia se basa en el efecto fotoeléctrico de los semiconductores. Su resistencia varía en función de la luz ambiental.

En presencia de luz, el material semiconductor absorbe la energía de los fotones, lo que da lugar a la producción de pares de electrones y huecos y aumenta la conductividad y reduce la resistencia. Cuanto más intensa es la luz, menor es la resistencia. Gracias a los cambios en la resistencia, es posible detectar la intensidad de la luz con precisión. Por este motivo, se utiliza ampliamente en sistemas de iluminación automática, control fotoeléctrico, monitorización en tiempo real y regulación de la luz.

<FONT COLOR=#BB00FF><font size="5"><b>Resistencia LDR</font color></font size></b>

Existe un tipo de resistencia especial denominado fotoresistencia o fotoresistor que es un componente electrónico cuya resistencia disminuye de forma exponencial con el aumento de la intensidad de luz incidente. Las siglas LDR vienen de su nombre en inglés, que es Light Dependent Resistor. En la imagen siguiente tenemos el símbolo, el aspecto real de una LDR y su curva característica de variación de resistencia con la iluminación.

![Símbolo, aspecto y curva característica de la LDR](../img/MB/simbolo_aspecto_curva_LDR.png){.center-img100}

### <FONT COLOR=#AA0000>Bloques</font>

==**De la clase Coding Box:**==

El bloque "cb nivel de luz" lee el valor analógico de la fotorresistencia. Cuanto más intensa sea la luz, mayor será el valor analógico (rango de valores analógicos: 0-1023).

![Bloque](../img/MB/cb_nivel_luz.png){.center-img20}

### <FONT COLOR=#AA0000>Prueba del código</font>
Puedes crear los bloques manualmente o abrir directamente el archivo de código que te puedes descargar del enlace: [5. Fotoresistencia o LDR](../programas/MB/5_Fotoresistencia.ubp).

El programa es el siguiente:

<center>

![5. Fotoresistencia o LDR](../img/MB/5_Fotoresistencia.png)  
***[5. Fotoresistencia o LDR](../programas/MB/5_Fotoresistencia.ubp)***

</center>

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Conecta Coding Box a MicroBlocks mediante USB o Bluetooth y haz clic en el botón "ejecutar" para cargar el código en la misma. Haz clic en el icono de graficado de datos ![icono](../img/MB/ico_graf.png) para mostrar el gráfico. Cubre el sensor con la mano y verás el valor decrecer.

![Resultado 5. Fotoresistencia o LDR](../img/MB/R5_Fotoresistencia.png){.center-img75}

![Resultado 5. Fotoresistencia o LDR](../img/MB/R5_Fotoresistencia_graf.png){.center-img75}