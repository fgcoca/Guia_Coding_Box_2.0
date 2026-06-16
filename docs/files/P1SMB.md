## <FONT COLOR=#007575>**1. Semáforo**</font>
### <FONT COLOR=#AA0000>Resumen</font>
El semáforo sirve para regular el paso de peatones y vehículos. En su versión más básica, tiene una luz roja, una amarilla y una verde que indican diferentes instrucciones.

* La luz roja indica Stop: los peatones y los vehículos deben detenerse.
* Amarillo para Precaución: peatones y conductores deben prepararse para detenerse. Si se está circulando, se debe reducir la velocidad.
* Verde para Adelante: peatones y vehículos pueden continuar circulando, pero deben respetar las normas de tráfico.

En este proyecto, vas a programar la ESP32 Coding Box para controlar un semáforo en miniatura. Por ejemplo, puedes configurar la duración de cada luz y el intervalo de tiempo entre ellas.

### <FONT COLOR=#AA0000>Ordinograma</font>

![1. Semáforo](../img/MB/1_diagrama_semaforo.png){.center-img} 

### <FONT COLOR=#AA0000>Bloques</font>

==**De Control:**==

* ![Bloque](../img/SMB/B_bucle.png) repite la ejecución un número determinado de veces. Solo tienes que introducir el número de repeticiones que necesites en el cuadro blanco.

==**Comentarios:**==

A veces es conveniente añadir un comentario a un bloque y para hacerlo desplegamos las opciones del bloque pinchando con el botón derecho y añadimos un comentario pinchando en el icono del interrogante

![Comentario](../img/SMB/comentario.png){.center-img100}

### <FONT COLOR=#AA0000>Prueba del código</font>
Puedes crear los bloques manualmente o abrir directamente el archivo de código que te puedes descargar del enlace: [1. Semáforo](../programas/SMB/Proy/P1SMB.abp).

El programa es el siguiente:

![1. Semáforo](../img/SMB/1_Semaforo.png){.center-img100}
[1. Semáforo](../programas/SMB/Proy/P1SMB.abp){.enlace-centrado}

### <FONT COLOR=#AA0000>Resultado de la prueba</font>
Conecta Coding Box a STEAMakersBlocks mediante un cable USB, por en marcha "Connector" y haz clic en el botón "Subir" para cargar el código. Verás que el LED verde se enciende durante 5 segundos y luego se apaga. Inmediatamente después, el LED amarillo parpadea tres veces. A continuación, el LED rojo se enciende durante 5 segundos y luego se apaga. Este funcionamiento imita exactamente el de un semáforo y se repetirá indefinidamente.
