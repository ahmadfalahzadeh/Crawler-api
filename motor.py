import os
##
# @package MyModule Module documentation
#

## Documentation for MOTOR class.
#
#  More details.
class MOTOR:
    
    ## The constructor.
    #  @param self The object pointer.
    #  @param GPIO_DIR: GPIO number which manages the direction of rotation of the motor
    #  @type GPIO_DIR: int
    #  @param GPIO_IO2 : GPIO number that manages whether or not the motir is activated
    #  @type GPIO_IO2: int
    #  @param PWM: number of the PWM
    #  @type PWM: int
    def __init__(self,GPIO_DIR, GPIO_IO2, PWM):
        self.GPIO_DIR_number = GPIO_DIR
        self.GPIO_IO2_number = GPIO_IO2
        self.PWM_number = PWM

    
    ## Documentation for a method.
    #  initializes a GPIO
    #  @param self The object pointer.
    #  @param GPIO_number: GPIO number to initialized 
    #  @type GPIO_number: int



    def init_GPIO(self,GPIO_number):
        if os.path.exists("/sys/class/gpio/gpio" + str(GPIO_number) + "/direction") == False:
            command1 = "echo "  + str(GPIO_number)  +" > /sys/class/gpio/export"
            command2 = "echo out > /sys/class/gpio/gpio" + str(GPIO_number) + "/direction"
            command3 = "chown www-data:www-data /sys/class/gpio/gpio%d/value" % GPIO_number #Enoc added this
            os.system(command1)
            os.system(command2)
            os.system(command3)
	

            

    ## Documentation for init_PWM_2 method.
    #  initializes the two PWMs
    #  warning: with odroid-C2 impossible to initialize a PWM then the second. Both are therefore initialized simultaneously
    #  @param self The object pointer.
    def init_PWM_2(self):
		#MODIFICAT 17-09-2020 11.09#
        command1 = "sudo modprobe pwm-meson npwm=2"
        command2 = "sudo modprobe pwm-ctrl"
        #command1 = "modprobe pwm-meson npwm=2"
        #command2 = "modprobe pwm-ctrl"
        command3 = "echo 10000 > /sys/devices/platform/pwm-ctrl/freq0"
        
        command5 = "echo 10000 > /sys/devices/platform/pwm-ctrl/freq1"
        #command6 = "echo 1 > /sys/devices/platform/pwm-ctrl/enable1"
        os.system(command1)
        os.system(command2)
        os.system(command3)
        
        os.system(command5)
        #os.system(command6)

    ## Documentation for enable_PWM method.
    #  enable or disable a PWM
    #  @param self The object pointer.
    #  @param on_off: 1 for enable, 0 for disable
    #  @type on_off: int
    #  @param R_L: 0 for the PWM of the right motor, 1 for the PWM of the left motor
    #  @type R_L: int
    def enable_PWM(self,on_off,R_L):
        command4 = "echo "+str(on_off)+" > /sys/devices/platform/pwm-ctrl/enable"+str(R_L)
        os.system(command4)

    ## Documentation for DIR method.
    #  determines the direction of rotation of the motor
    #  @param self The object pointer.
    #  @param GPIO_number: direction GPIO number (GPIO_DIR)
    #  @type R_L: int
    #  @param direction: 0 for clockwise, 1 for trigonometric
    #  @type direction: int
    def DIR(self,GPIO_number, direction):
        command1 = "echo "+ str(direction)+ " >/sys/class/gpio/gpio"+str(GPIO_number)+"/value"
        os.system(command1)

    ## Documentation for IO2 method.
    #  enable or disable a motor
    #  @param self The object pointer.
    #  @param GPIO_number: GPIO number (GPIO_IO2)
    #  @type GPIO_number: int
    #  @param direction: 0 for disable, 1 for enable
    #  @type direction: int
    def IO2(self,GPIO_number, motor_on_off):
        command1 = "echo "+ str(motor_on_off) + " >/sys/class/gpio/gpio"+str(GPIO_number)+"/value"
        os.system(command1)

    ## Documentation for duty_cycle method.
    #  determines the motor speed
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the motor speed (0 to 100)
    #  @type duty_cycle: int
    #  @param PWM_number: 0 for right motor, 1 for left motor
    #  @type PWM_number: int
    def duty_cycle(self, duty_cycle, PWM_number):
		#MODIFICAT 17/09/2020 12:19#
        command2 = "echo " + str(int((float(duty_cycle)/100)*1023)) + " > /sys/devices/platform/pwm-ctrl/duty"+ str(PWM_number)

	################duty 0 problem
        if int(duty_cycle) == 0: 
            disable_command = "echo 0 > /sys/devices/platform/pwm-ctrl/enable" + str(PWM_number)
            os.system(disable_command)

        else: 
            enable_command ="echo 1 > /sys/devices/platform/pwm-ctrl/enable" + str(PWM_number)
            os.system(enable_command)


        #command2 = "echo " + str(int(((100-int(duty_cycle))/100)*1023)+1) + " > /sys/devices/platform/pwm-ctrl/duty"+ str(PWM_number)
		#command2 = "echo " + str(int((int(duty_cycle)/100)*1023)+1) + " > /sys/devices/platform/pwm-ctrl/duty"+ str(PWM_number)
        os.system(command2)


