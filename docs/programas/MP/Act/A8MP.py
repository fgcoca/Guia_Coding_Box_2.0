'''
 * Archivo         : A8MP
 * Versión Thonny  : Thonny 5.0.0
'''
import machine
import time
#importa mfrc522 desde mfrc522_i2c
from mfrc522_i2c import mfrc522

#configura el I2C
dir = 0x28		#dirección física del RFID I2C
scl = 22		#pin SCL del IIC
sda = 21		#pin SDA del IIC

#crea un objeto MFRC522 con la dirección, y los pines SCL y SDA
rc522 = mfrc522(scl, sda, dir)
#Inicializar el módulo MFRC522; imprescindible para garantizar su funcionamiento.
rc522.PCD_Init()
'''
muestra la información leida por MFRC522
utilizada para depurar y comprobar su correcto funcionamiento
'''
rc522.ShowReaderDetails()        

while True:
    #detecta si hay una tarjeta RFID en el área de detección
    if rc522.PICC_IsNewCardPresent():
        #Intenta leer el ID de la tarjeta. Si se lee correctamente, devuelve "True"
        if rc522.PICC_ReadCardSerial() == True:
            #Imprime "UID de la tarjeta:" y el UID
            print("UID de la tarjeta:",rc522.uid.uidByte[0 : rc522.uid.size])
