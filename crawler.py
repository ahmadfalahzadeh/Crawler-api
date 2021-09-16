import os
import sys
import config
from motor import MOTOR

## Documentation for CRAWLER class.
#
#  More details.
class CRAWLER():
    ## The constructor.
    def __init__(self):
        self.MR = MOTOR(config.motor_right_IO2,config.motor_right_DIR,0)
        self.ML = MOTOR(config.motor_left_IO2,config.motor_left_DIR,1)

    ## Documentation for init_I02_DIR method.
    #  initializes GPIOs for both motors
    #  @param self The object pointer.
    def init_IO2_DIR(self):
        self.MR.init_GPIO(config.motor_right_IO2)
        self.ML.init_GPIO(config.motor_left_IO2)
        self.MR.init_GPIO(config.motor_right_DIR)
        self.ML.init_GPIO(config.motor_left_DIR)

    ## Documentation for init_I02_DIR method.
    #  @param self The object pointer.
    def init_PWM(self): #ne sert a rien
        self.MR.init_PWM_2()

    ## Documentation for PWM method.
    #  enables or disables PWMs
    #  @param self The object pointer.
    #  @param on_off: 1 to activate PWM, 0 to deactivate PWM
    #  @type on_off: int
    def PWM(self,on_off):
        self.MR.enable_PWM(on_off,config.motor_right_PWM)
        self.ML.enable_PWM(on_off,config.motor_left_PWM)

    ## Documentation for on_off method.
    #  enables or disables motors
    #  @param self The object pointer.
    #  @param motor_on_off: 1 to activate motors, 0 to deactivate motors
    #  @type motor_on_off: int
    def on_off(self, motor_on_off):
        self.MR.IO2(config.motor_left_IO2, motor_on_off)
        self.ML.IO2(config.motor_right_IO2, motor_on_off)   

    ## Documentation for forward method.
    #  moves forward the robot at variable speed
    #  warning: a speed lower than 50%, can cause a speed difference between the two motors
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the robot speed (0 to 100)
    #  @type duty_cycle: int
    def forward(self, duty_cycle):     
        self.MR.DIR(config.motor_right_DIR, int(0))   #0
        self.ML.DIR(config.motor_left_DIR, int(1))    #1
        self.MR.duty_cycle(duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)
        print("[+] I should be going forward from CR.py")

    ## Documentation for backward method.
    #  moves backward the robot at variable speed
    #  warning: a speed lower than 50%, can cause a speed difference between the two motors
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the robot speed (0 to 100)
    #  @type duty_cycle: int
    def backward(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 1)
        self.ML.DIR(config.motor_left_DIR, 0)
        self.MR.duty_cycle( duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle( duty_cycle, config.motor_left_PWM)

    ## Documentation for right method.
    #  rotates the robot on itself to the right (clockwise) at variable speed
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the robot speed (0 to 100)
    #  @type duty_cycle: int
    def right(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 0)
        self.ML.DIR(config.motor_left_DIR, 0)
        self.MR.duty_cycle( duty_cycle, config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)

    ## Documentation for left method.
    #  rotates the robot on itself to the left (trigonometric direction) at variable speed
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the robot speed (0 to 100)
    #  @type duty_cycle: int
    def left(self, duty_cycle):
        self.MR.DIR(config.motor_right_DIR, 1)
        self.ML.DIR(config.motor_left_DIR, 1)
        self.MR.duty_cycle( duty_cycle,config.motor_right_PWM)
        self.ML.duty_cycle(duty_cycle, config.motor_left_PWM)

    ## Documentation for init_light method.
    #  unfinished function
    #  @param self The object pointer.
    def init_light(self):
        self.MR.init_GPIO(config.light1)
        self.MR.init_GPIO(config.light2)
        self.MR.init_GPIO(config.light3)

    ## Documentation for init_I02_DIR method.
    #  unfinished function
    #  @param self The object pointer.
    #  @param on_off: 1 to activate light, 0 to deactivate light
    #  @type on_off: int
    def light_on_off(self, on_off):
        command1 = "echo "+ str(on_off) + " >/sys/class/gpio/gpio"+str(config.light1)+"/value"
        os.system(command1)
        command2 = "echo "+ str(on_off) + " >/sys/class/gpio/gpio"+str(config.light2)+"/value"
        os.system(command2)
        command3 = "echo "+ str(on_off) + " >/sys/class/gpio/gpio"+str(config.light3)+"/value"
        os.system(command3)
	




