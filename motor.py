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
    def __init__(self, GPIO_IO2,GPIO_DIR, PWM):
        self.GPIO_DIR_number = GPIO_DIR
        self.GPIO_IO2_number = GPIO_IO2
        self.PWM_number = PWM
        print("MOTOR __init__")

################################################# INIT METHOD GPIO ##################################################################     

    ## Documentation for a method.
    #  initializes a GPIO
    #  @param self The object pointer.
    #  @param GPIO_number: GPIO number to initialized 
    #  @type GPIO_number: int


    def init_GPIO(self,GPIO_number):
        print("-----> Init GPIO %d" % GPIO_number)
        if os.path.exists("/sys/class/gpio/gpio" + str(GPIO_number) + "/direction") == False:
            print("-----> Init GPIO %d" % GPIO_number)
            command1 = "sudo chown -R www-data:www-data /sys/class/gpio"
            command2 = "echo "  + str(GPIO_number)  +" > /sys/class/gpio/export"
            command3 = "sudo chown -R www-data:www-data /sys/class/gpio/gpio"+str(GPIO_number)+"/*"
            command4 = "echo out > /sys/class/gpio/gpio" + str(GPIO_number) + "/direction"
            print("-----> Direction GPIO %d" % GPIO_number)
            os.system(command1)
            os.system(command2)
            os.system(command3)
            os.system(command4) 
	

################################################# INIT METHOD PWM ##################################################################             

    ## Documentation for init_PWM_2 method.
    #  initializes the two PWMs
    #  warning: with www-data-C2 impossible to initialize a PWM then the second. Both are therefore initialized simultaneously
    #  @param self The object pointer.
    def init_PWM_2(self,PWM_number):
        print("-----> Init PWM ")
        #www-data C4
        if os.path.exists("/sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/period")==False:
            command1 = "sudo chown -R www-data:www-data /sys/class/pwm/pwmchip0/"
            command2= "sudo echo "+str(PWM_number)+" > /sys/class/pwm/pwmchip0/export" #pin 12 motor Right, pin 15 motor Left
            command3 = "sudo chown -R www-data:www-data /sys/class/pwm/pwmchip0/*"
            command4= "sudo echo 100000 > /sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/period" # 10 kHz
        
            os.system(command1)
            os.system(command2)
            print("PWM EXPORTED")
            print("pwm ready: %d" % PWM_number)
            os.system(command3)
            os.system(command4)
            print("PWM PERIOD SET")

#################################################### PWM ENABLE MOTOR RIGHT AND LEFT ##############################################
    ## Documentation for enable_PWM method.
    #  enable or disable a PWM
    #  @param self The object pointer.
    #  @param on_off: 1 for enable, 0 for disable
    #  @type on_off: int
    def enable_PWM(self,on_off,PWM_number):
        print("PWM ENABLE %d" %on_off)
        print("PWM ENABLE %d" %PWM_number)
        command1= "sudo echo "+str(on_off)+" > /sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/enable"
        os.system(command1)
        
################################################# DIR METHOD GPIO ##################################################################        

    ## Documentation for DIR method.
    #  determines the direction of rotation of the motor
    #  @param self The object pointer.
    #  @param GPIO_number: direction GPIO number (GPIO_DIR)
    #  @type R_L: int
    #  @param direction: 0 for clockwise, 1 for trigonometric
    #  @type direction: int
    def DIR(self,GPIO_number, direction):
        command1 = "echo "+ str(direction)+ " >/sys/class/gpio/gpio"+str(GPIO_number)+"/value"
        print("-----> GPIO %d" % GPIO_number,"-->Direction %d" %direction)
        os.system(command1)
        
        
################################################# IO2 METHOD GPIO ################################################################## 

    ## Documentation for IO2 method.
    #  enable or disable a motor
    #  @param self The object pointer.
    #  @param GPIO_number: GPIO number (GPIO_IO2)
    #  @type GPIO_number: int
    #  @param direction: 0 for disable, 1 for enable
    #  @type direction: int
    def IO2(self,GPIO_number, motor_on_off):
        command1 = "echo "+ str(motor_on_off) + " >/sys/class/gpio/gpio"+str(GPIO_number)+"/value"
        print("-----> GPIO %d" % GPIO_number, "-->Value %d" %motor_on_off)
        os.system(command1)


     ## Documentation for read_GPIO.
    #  read GPIO and return the value
    #  @param self The object pointer.
    def read_GPIO(self, GPIO_number):
        print ("----------------> Read GPIO <------------------")
        command1 = "cat /sys/class/gpio/gpio" + str(GPIO_number) + "/value"
        os.system(command1)
        read = int(os.popen(command1).read())
        print("GPIO NUMBER: %d" %GPIO_number)
        print ("GPIO READ VALUE :  %d" % read)
        return read
        
        
        
################################################# DUTY CYCLE METHOD PWM ##################################################################

    ## Documentation for duty_cycle method.
    #  determines the motor speed
    #  @param self The object pointer.
    #  @param duty_cycle: percentage value of the motor speed (0 to 100)
    #  @type duty_cycle: int
    #  @¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡¡ OJO-->must have duty_cycle < period !!!!!!!!!!!!!!!! (period defined in init_PWM_2 method )
    #◘ @18000000 is the max period of PWM
  
    def duty_cycle(self, duty_cycle,PWM_number):
        command1= "echo "+str(int((float(duty_cycle)/100)*80000))+" > /sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/duty_cycle" #duty in % converted in ns
        
        if int(duty_cycle) == 0 :
            disable_PWM= "echo 0 > /sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/enable"
            os.system(disable_PWM)
            print("I DISABLE PWM R BECAUSE DUTY=0")
        else :
            enable_PWM= "echo 1 > /sys/class/pwm/pwmchip0/pwm"+str(PWM_number)+"/enable"
            os.system(enable_PWM)
            print("I ENABLE PWM L BECAUSE DUTY/=0")
         
        os.system(command1)
