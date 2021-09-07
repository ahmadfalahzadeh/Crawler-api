import smbus
import os


## Documentation for COMPASS class.
#
#  More details.
class COMPASS:
    
    ## The constructor.
    def __init__(self,adress):
        self.adress = adress
        self.bus = smbus.SMBus(1)

    ## Documentation for init_I2C method.
    #  @param self The object pointer.
    def init_I2C(self):
        if os.path.exists("/dev/i2c-1") == False:
            commande1 = "modprobe aml_i2c"
            os.system(commande1)

    ## Documentation for bearing255 method.
    #  @param self The object pointer.
    #  @return: returns the value of the compass, value coded on a byte (0 to 255)
    #  @type: int
    def bearing255(self):
        bear = self.bus.read_byte_data(self.adress, 1)
        return bear

    ## Documentation for bearing3599 method.
    #  @param self The object pointer.
    #  @return: returns the value of the compass, coded value from 0 to 359.9, step of 0.1 degree
    #  @type: int
    def bearing3599(self):
        bear1= self.bus.read_byte_data(self.adress, 2)
        bear2= self.bus.read_byte_data(self.adress, 3)
        bear = (bear1 << 8) +bear2
        bear = bear/10.0
        return bear
		    
