'''
 * Archivo         : A13MP
 * Versión Thonny  : Thonny 5.0.0
------------------------------------------------------
Tabla lógica de giro del motor:
------------------------------------------------------
  IO17(INA) | IO18(INB)  | estado del motor	         |
------------------------------------------------------ 
   Alto (H) |  Bajo (L)  | Gira en sentido contrario |
------------------------------------------------------
   Bajo (L) |  Alto (H)  | Gira en hacia delante     |
------------------------------------------------------
  Alto (H)  |  Alto (H)  | parada gradual            |
------------------------------------------------------
   Bajo (L) |  Bajo (L)  | freno a tope              |
------------------------------------------------------
'''

from machine import Pin
import time

#pin de control INA es IO17
INA = Pin(17,Pin.OUT)
#pin de control INB es IO18
INB = Pin(18,Pin.OUT)

while True:
    #adelante
    INA.off()
    INB.on()
    time.sleep(2)
    #atras
    INA.on()
    INB.off()
    time.sleep(2)
    #parar
    INA.off()
    INB.off()
    time.sleep(2)
