import smbus
import time
import os

class COMPASS:
    
    def __init__(self,adress):
        self.adress = adress
        #self.bus = smbus.SMBus(1)
    def init_I2C(self):
        fichier = open("data.txt", "a")
        fichier.write("I2C initialisation")
        fichier.close()
    def bearing255(self):
        bear = 100
        return bear

    def bearing3599(self):
        bear = 100.1
        fichier = open("data.txt", "a")
        fichier.write(str(bear) +"\n")
        fichier.close()
        return bear

		    