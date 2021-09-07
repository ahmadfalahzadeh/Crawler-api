#import
import os

#to get config, crawler and motor from another folder
import sys
sys.path.insert(1, '/var/www/api')

import config
from time import sleep
from crawler import CRAWLER
from motor import MOTOR

#call classes
## crawler type object
CR = CRAWLER()
## motor type object (motor right)
MR = MOTOR(config.motor_right_IO2,config.motor_right_DIR,0)
## motor type object (motor left)
ML = MOTOR(config.motor_left_IO2,config.motor_left_DIR,1)

#initialization PWM
CR.init_PWM()

#enable PWM
CR.PWM(1) 

#duty cycle of PWM
print('speed1:')
speed1=input()
print('speed2:')
speed2=input()
MR.duty_cycle(speed1,config.motor_right_PWM) #right motor
ML.duty_cycle(speed2,config.motor_left_PWM) #left motor
       
