import os
import sys
import config
from motor_test import MOTOR
from compass_test import COMPASS


class CRAWLER():
    def __init__(self):
        self.MR = MOTOR(config.motor_right_IO2,config.motor_right_DIR,0)
        self.ML = MOTOR(config.motor_left_IO2,config.motor_left_DIR,1)
        self.CP = COMPASS(config.I2C_adresse)

    def init_IO2_DIR(self):
        self.MR.init_GPIO(config.motor_right_IO2)
        self.ML.init_GPIO(config.motor_left_IO2)
        self.MR.init_GPIO(config.motor_right_DIR)
        self.ML.init_GPIO(config.motor_left_DIR)

    def init_PWM(self): #ne sert a rien
        self.MR.init_PWM_2()

    def PWM(self,on_off):
        self.MR.enable_PWM(on_off,config.motor_right_PWM)
        self.ML.enable_PWM(on_off,config.motor_left_PWM)

    def on_off(self, motor_on_off):
        self.MR.IO2(config.motor_left_IO2, motor_on_off)
        self.ML.IO2(config.motor_right_IO2, motor_on_off)   

    def forward(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 0)
        self.ML.DIR(config.motor_left_DIR, 1)
        self.MR.duty_cycle(duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)

    def backward(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 1)
        self.ML.DIR(config.motor_left_DIR, 0)
        self.MR.duty_cycle( duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle( duty_cycle, config.motor_left_PWM)

    def right(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 0)
        self.ML.DIR(config.motor_left_DIR, 0)
        self.MR.duty_cycle( duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)

    def left(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 1)
        self.ML.DIR(config.motor_left_DIR, 1)
        self.MR.duty_cycle( duty_cycle,config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)

    def init_light(self):
        self.MR.init_GPIO(config.light1)
        self.MR.init_GPIO(config.light2)
        self.MR.init_GPIO(config.light3)

    def light_on_off(self, on_off):
        if motor_on_off == 1:
            dir = "ON"
        elif motor_on_off== 0:
            dir = "OFF"
        else :
            dir = "error"
        fichier = open("data.txt", "a")
        fichier.write("Light is "+dir)
        fichier.close()

    def cmd_direction(self, value_direction):
        fichier = open("data.txt", "a")
        fichier.write("Mise en place du robot")
        fichier.close()

    def read_data(self):
        with open("data.txt", "r") as fs:
            lignes = [ligne.rstrip() for ligne in fs.readlines()]
        lignes = lignes[-10:]
        return str(lignes)


