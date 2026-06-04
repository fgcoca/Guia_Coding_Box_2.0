## <FONT COLOR=#007575>**4. Amplificador**</font>
### <FONT COLOR=#AA0000>Resumen</font>
El módulo amplificador de potencia integrado es un altavoz y el amplificador de audio 8002B. El chip es un amplificador de 2W clase AB capaz de entregar los 2W de potencia a una carga de tres ohmios con una distorsión menor al 10% a partir de una alimentación de 5V. Típicamente el amplificador entrega en torno a los 2W para una carga de ocho ohmios.

Externamente en Coding Box solamente vemos el altavoz

![Altavoz](../img/MB/Altavoz.png){.center-img20}

### <FONT COLOR=#AA0000>Bloques</font>
==**De Actuadores:**==

* ![Bloque](../img/SMB/B_zumbador.png) Reproduce durante el tiempo especificado la frecuencia indicada. El pin asociado es el GPIO32.
* ![Bloque](../img/SMB/B_tono.png) Para establecer en frecuencia las notas de la escala musical incluidos los sostenidos.
* ![Bloque](../img/SMB/B_zumbador_RTTTL.png) Para reproducir la melodia RTTTL que introduzcas en "song:".

???+ info "RTTTL"
    Si despliegas el menú asociado a la 'llave' o herramienta encontrarás la entrada [RTTTL Info](https://www.steamakersblocks.com/web/help/rtttl) donde puedes encontrar información referida a este formato y acceder a muchas melodias conocidas en formato RTTTL.

    También podemos acceder a esta información haciendo clic derecho sobre el bloque y escogiendo la opción "Ayuda" de entre las mostradas en la ventana emergente.

* ![Bloque](../img/SMB/B_RTTTL_melodias.png) Para seleccionar de la lista alguna de las melodias prefijadas.

### <FONT COLOR=#AA0000>Prueba del código</font>
Puedes crear los bloques manualmente o abrir directamente el archivo de código que te puedes descargar del enlace: [4. Amplificador - A4SMB](../programas/SMB/Act/A4SMB.abp).

El programa es el siguiente:

<center>

![4. Amplificador - A4SMB](../img/SMB/4_Amplificador.png)  
***[4. Amplificador - A4SMB](../programas/SMB/Act/A4SMB.abp)***

</center>

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Conecta Coding Box a STEAMakersBlocks mediante un cable USB, por en marcha "Connector" y haz clic en el botón "Subir" para cargar el código. El amplificador de potencia reproduce al inicio la melodia de Star Wars y las notas Do, Re, Mi, Fa, Sol, La y Si en bucle.
