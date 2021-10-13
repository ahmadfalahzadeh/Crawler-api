## PWM number for the right motor
motor_right_PWM = 0

## GPIO number determining the direction of rotation for the right motor
#  connect to the DIR pin of the microcontroller right
motor_right_DIR = 476 #pin 16 odroid c4
# another pin for little robot test
motor_right_DIR2= 477 #•pin 18 odroid c4
#motor_right_DIR = 225 #pin 13 frito! cambio por pin 12 (238) pin 12  tambien frito cambio por pin 26 (225) odroid c2

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller right
motor_right_IO2 = 479 #pin 11 odroid c4
#motor_right_IO2 = 247 #pin 11 odroid c2




## PWM number for the left motor
motor_left_PWM = 1

## GPIO number determining the direction of rotation for the left motor
#  connect to the DIR pin of the microcontroller left
motor_left_DIR = 480 #pin 13 odroid c4
# another pin for little robot test
motor_left_DIR2=481 #↕pin 7 odroid c4
#motor_left_DIR = 237 #pin 15 odroid c2

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller left
motor_left_IO2 = 478 #pin 22 odroid c4
#motor_left_IO2 = 230 #pin 23 odroid c2





## number of the first GPIO for light
light1 = 490 #pin 29 odroid c4
#light1 = 228 #pin 29 odroid c2
## number of the second GPIO for light
light2 = 491 #pin 31 odroid c4
#light2 = 219 #pin 31 odroid c2
## number of the third GPIO for light
light3 = 434 #pin 32 odroid c4
#light3 = 214 #pin 35 odroid c2
## compass address
I2C_adresse = 0x60

# compass accuracy
compass_accuracy = 5
