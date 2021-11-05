##This is config file
## PWM number for the right motor

#hgsukydguyfgvbuertvgvufgjhdchgjawhbfjhfhgsdkygvjsgdck
motor_right_PWM = 0 #pin 12

## GPIO number determining the direction of rotation for the right motor
#  connect to the DIR pin of the microcontroller right
motor_right_DIR = 476 #pin 16 odroid c4
#motor_right_DIR2= 477 #•pin 18 odroid c4 # another pin for little robot test

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller right
motor_right_IO2 = 433 #pin 26 odroid c4


## PWM number for the left motor
motor_left_PWM = 1 #pin 15

## GPIO number determining the direction of rotation for the left motor
#  connect to the DIR pin of the microcontroller left
motor_left_DIR = 480 #pin 13 odroid c4
#motor_left_DIR2=481 #↕pin 7 odroid c4 # another pin for little robot test

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller left
motor_left_IO2 = 478 #pin 22 odroid c4



## number of the first GPIO for light
light1 = 490 #pin 29 odroid c4 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! NOT USED IN THE HARDWARE (only 2 lights)
## number of the second GPIO for light
light2 = 491 #pin 31 odroid c4
## number of the third GPIO for light
light3 = 434 #pin 32 odroid c4

## compass address
I2C_adresse = 0x60

# compass accuracy
compass_accuracy = 5
