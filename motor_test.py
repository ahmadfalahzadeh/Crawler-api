import os
import sys

class MOTOR:
    
    def __init__(self,GPIO_DIR, GPIO_IO2, PWM):
        self.GPIO_DIR_number = GPIO_DIR
        self.GPIO_IO2_number = GPIO_IO2
        self.PWM_number = PWM

    def init_GPIO(self,GPIO_number):
        fichier = open("data.txt", "a")
        fichier.write("Initialisation du GPIO " + str(GPIO_number)+"\n")
        fichier.close()

    def init_PWM_2(self):
        fichier = open("data.txt", "a")
        fichier.write("Initialisation des PWMs , Frequence 1kHz \n")
        fichier.close()
        

    def enable_PWM(self,on_off,R_L):
        fichier = open("data.txt", "a")
        if on_off == 1:
            etat = "enable"
        elif on_off == 0:
            etat = "disable"
        else :
            etat = "error"
        if R_L == 1:
            coter = "Right"
        elif R_L == 2:
            coter = "Left"
        else :
            coter = "error"

        fichier.write("PWM "+coter+" is "+etat+"\n")
        fichier.close()

    def DIR(self,GPIO_number, direction):
        if direction == 0:
            dir = "forward"
        elif direction == 1:
            dir = "backward"
        else :
            dir = "error"
        fichier = open("data.txt", "a")
        fichier.write("GPIO "+str(GPIO_number)+" direction : "+str(dir)+"\n")
        fichier.close()

    def IO2(self,GPIO_number, motor_on_off):
        if motor_on_off == 1:
            dir = "ON"
        elif motor_on_off== 0:
            dir = "OFF"
        else :
            dir  = "error"
        fichier = open("data.txt", "a")
        fichier.write("GPIO "+GPIO_number+" is "+dir+"\n")
        fichier.close()

    def duty_cycle(self, duty_cycle, PWM_number):
        fichier = open("data.txt", "a")
        if PWM_number == 0:
            coter = "Right"
        elif PWM_number == 1:
            coter = "Left"
        else :
            coter = "error"

        fichier.write("PWM "+str(coter)+" speed : "+str(duty_cycle)+"\n")
        fichier.close()


M = MOTOR(3,5,2)
M.init_GPIO(3)
M.init_PWM_2()
M.enable_PWM(1,2)
M.duty_cycle(50,1)
