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

#initialization GPIO
CR.init_IO2_DIR() #DIR & IO2
CR.init_light() #light GPIOs

#Write GPIO
MR.DIR(config.motor_right_DIR,0) #Pin & 0:clockwise, 1:counterclockwise
ML.DIR(config.motor_left_DIR,0) #Pin & 0:clockwise, 1:counterclockwise

MR.IO2(config.motor_right_IO2,0) #Pin & ON/OFF
ML.IO2(config.motor_left_IO2,0) #Pin & ON/OFF

CR.light_on_off(0)







