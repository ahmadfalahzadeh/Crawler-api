## PWM number for the right motor
motor_right_PWM = 0

## GPIO number determining the direction of rotation for the right motor
#  connect to the DIR pin of the microcontroller right
motor_right_DIR = 225 #pin 13 frito! cambio por pin 12 (238) pin 12  tambien frito cambio por pin 26 (225)

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller right
motor_right_IO2 = 247 #pin 11




## PWM number for the left motor
motor_left_PWM = 1

## GPIO number determining the direction of rotation for the left motor
#  connect to the DIR pin of the microcontroller left
motor_left_DIR = 237 #pin 15

## GPIO number determining whether the motor is enabled or not
#  connect to the IO2 pin of the microcontroller left
motor_left_IO2 = 230 #pin 23





## number of the first GPIO for light
light1 = 228 #pin 29

## number of the second GPIO for light
light2 = 219 #pin 31

## number of the third GPIO for light
light3 = 214 #pin 35

## compass address
I2C_adresse = 0x60

# compass accuracy
compass_accuracy = 5
