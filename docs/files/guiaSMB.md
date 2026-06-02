**STEAMakersBlocks** dispone de infinidad de recursos de documentación sobre la utilización del IDE y las placas soportadas por la plataforma.

* [Acceso a la web de recursos](https://www.steamakersblocks.com/web/site/doc#)

El manejo de la plataforma es sencillo y está todo explicado en:

* [Libro sobre el manejo de STEAMakersBlocks](https://docs.google.com/document/u/1/d/e/2PACX-1vQSrOKHpbLQHVbGFdAvp7DcndoftoHDI20nvwGMaxu_7bGc1bUCmi4U6DZrJWRSudc2iXBg43QMuzCT/pub)

## <FONT COLOR=#007575>**Programando con STEAMakersBlocks**</font>
Para poder conectar y programar las placas con STEAMakersBlocks, es necesario instalar [Connector](https://www.steamakersblocks.com/web/site/abconnector) para permitir la comunicación entre el entorno STEAMakersBlocks y la placa electrónica.

En [Recursos](https://www.steamakersblocks.com/web/site/doc#) de [STEAMakersBlocks](https://www.steamakersblocks.com/) tenemos todas las opciones de descarga y condiciones de instalación de [Connector](https://www.steamakersblocks.com/web/site/abconnector) para los sistemas operativos soportados. Para el caso de Ubuntu nos indica:

![Connector](../img/SMB/Connector.png){.center-img75}

Una vez instalado lo podemos encontrar entre las aplicaciones:

![Connector](../img/SMB/Connector_app.png){.center-img75}

Al abrir Connector, aparece este cuadro de diálogo que va mostrando información sobre la placa y STEAMakersBlocks:

![Connector en ejecución](../img/SMB/Connector_eje.png){.center-img75}

</center>

Dejamos Connector en ejecución minimizado en segundo plano.
!!! Info "IMPORTANTE:"
    !!! Example ""
    Las imágenes pueden no corresponderse con la plataforma STEAMakersBlocks porque fueron capturadas cuando se llamaba ArduinoBlocks, pero básicamente el cambio estará en el logotipo.

El procedimiento de creación de programas es el siguiente:

<FONT size=9><FONT COLOR=#FF0055><b>1.</b></font></font> En **STEAMakersBlocks**, crea una cuenta pulsando en “Iniciar sesión” y, posteriormente, en “nuevo usuario”:

![Pantalla inicial STEAMakersBlocks](../img/SMB/pant_ini_AB.png){.center-img75}

</center>

!!! Success "Nuevas formas de acceso:"
    También es posible iniciar sesión utilizando una cuenta existente en Google o Microsoft
    !!! Question ""
        
    ![PAlternativas de acceso a STEAMakersBlocks](../img/SMB/pant_ini_accesos.png){.center-img} 

<FONT size=9><FONT COLOR=#FF0055><b>2. </b></font></font> Al entrar en la plataforma te encontrarás esta pantalla:

![Sesión iniciada en STEAMakersBlocks](../img/SMB/ses_ini.png){.center-img}

<FONT size=9><FONT COLOR=#FF0055><b>3.</b></font></font> Al hacer clic en "Empezar un nuevo proyecto!" aparece la siguiente pantalla para seleccionar el tipo de proyecto:

![Nuevo proyecto](../img/SMB/nuevo_proy.png){.center-img}

<FONT size=9><FONT COLOR=#FF0055><b>4.</b></font></font> Para crear un nuevo **proyecto personal**, debes rellenar un formulario. Para programar Coding Box 2.0 debes seleccionar ESP32 / WROOM en **Tipo de proyecto**.

![Tipo de proyecto](../img/SMB/tipo_proy.png){.center-img}

<FONT size=9><FONT COLOR=#FF0055><b>5.</b></font></font> Una vez creado el proyecto, después de haber cumplimentado su nombre y demás campos del formulario, se abre el entorno de programación:

![Proyecto creado](../img/SMB/creado_proy.png){.center-img}

<FONT size=9><FONT COLOR=#FF0055><b>6.</b></font></font> En la parte izquierda de esta pantalla, encontrarás los bloques disponibles clasificados por diferentes categorías. Por ejemplo, en la siguiente imagen puedes ver los bloques de algunos de los sensores que se pueden controlar.

![Algunos bloques de sensores](../img/SMB/B_sensores.png){.center-img}

<FONT size=9><FONT COLOR=#FF0055><b>7.</b></font></font> Arrastra los bloques al espacio de programación para programar tu placa. Por ejemplo, podemos programar el envío en bucle de un mensaje por puerto serie. El **puerto serie**, también conocido como puerto de comunicaciones serie o interfaz serie, es un tipo de conexión utilizada en ordenadores y dispositivos periféricos para la transferencia de datos. La característica principal del puerto serie es que envía los datos en serie; es decir, bit a bit, a través de un solo canal o hilo. Los bloques más importantes para utilizar el puerto serie son:

![Bloques puerto serie](../img/SMB/B_serie.png){.center-img75}

<FONT size=9><FONT COLOR=#FF0055><b>8.</b></font></font> Un programa de ejemplo sería así:

<center>

![Programa Hola mundo](../img/SMB/P_HolaMundo.png)  
***[Programa Hola mundo](../programas/SMB/HolaMundo.abp)***

</center>

Dentro de la estructura “**Inicializar**” colocamos el bloque de configuración de la velocidad de transferencia de datos (“**baudrate**”) del puerto serie a 115200. Y en el bucle principal, colocamos el bloque para enviar un mensaje en concreto, seleccionando que se realice un salto de línea. Para que el mensaje no se muestre tan rapidamente hacemos que se reproduzca cada cierto tiempo.

<FONT size=9><FONT COLOR=#FF0055><b>9.</b></font></font> Una vez creado el programa, debes transferirlo (subirlo) a la placa. Para ello, sigue los siguientes pasos:

* Comprueba que AB-Connector está ejecutańdose.
* Conecta la placa al ordenador mediante un cable USB.
* Selecciona el puerto de comunicación. Puedes conectar y desconectar el cable USB del ordenador para diferenciar cuál es el puerto de comunicación que utiliza la placa.
* Si no aparece el "/dev/ttyUSBn" directamente, pulsa en el icono de actualización. En entornos Linux, MacOS y Chromebook se muestra así el nombre. En Windows se muestra como COM.

![Establecer conexión USB](../img/SMB/P_conex.png){.center-img75}

* Pulsando en el botón “Subir”, carga el programa en la placa.

![Subir el programa a la placa](../img/SMB/P_subir.png){.center-img75}

!!! info "Tiempo de subida"
    En ESP32 el tiempo de subida será bastante mayor que en otras placas debido a la cantidad y peso de las librerias que utiliza ESP32.

Para poder visualizar el monitor serie y comprobar qué mensajes está enviando la placa al ordenador, debes abrirlo en tu entorno de programación, pulsando el botón “Consola”:

![Abrir consola serie](../img/SMB/P_abre_consola.png){.center-img75}

<FONT size=9><FONT COLOR=#FF0055><b>10.</b></font></font> Se abrirá la ventana siguiente:

![Consola serie](../img/SMB/consola.png){.center-img100}

<FONT size=9><FONT COLOR=#FF0055><b>11.</b></font></font> Selecciona la tasa de baudios (velocidad de transmisión de datos) con la que has iniciado el puerto serie y después haz clic en conectar. Verás el resultado en pantalla.

![Consola serie recibiendo datos](../img/SMB/consola_recibe.png)  
