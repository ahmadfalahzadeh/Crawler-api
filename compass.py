import smbus
import os


## Documentation for COMPASS class.
#
#  More details.
class COMPASS:
    
    
    ## The constructor.
    def __init__(self,adress):
        try:
            self.init_I2C()
            self.adress = adress 
            self.bus = smbus.SMBus(1)
            self.connected=True
            self.bus.read_byte_data(self.adress, 1)
        except Exception as e:
            print("!!!!!!!!!!!!!!!COMPASS NOT CONNECTED!!!!!!!!!!!!!!!")
            print(e)
            self.connected=False

    ## Documentation for init_I2C method.
    #  @param self The object pointer.
    def init_I2C(self):
        commande1="sudo chown -R www-data:i2c /sys/bus/i2c"
        os.system(commande1)

    ## Documentation for bearing255 method.
    #  @param self The object pointer.
    #  @return: returns the value of the compass, value coded on a byte (0 to 255)
    #  @type: int
    def bearing255(self):
        if self.connected==True:
            bear = self.bus.read_byte_data(self.adress, 1)
            return bear

        else:
            print("compass disconnected")
            return 0
       

    ## Documentation for bearing3599 method.
    #  @param self The object pointer.
    #  @return: returns the value of the compass, coded value from 0 to 359.9, step of 0.1 degree
    #  @type: int
    def bearing3599(self):
        if self.connected==True:
            bear1= self.bus.read_byte_data(self.adress, 2)
            bear2= self.bus.read_byte_data(self.adress, 3)
            bear = (bear1 << 8) +bear2
            bear = bear/10.0
            return bear

        else:
            print("compass disconnected")
            return 0
           
		    
if __name__=="__main__":
    print("compass test")
    compass=COMPASS(0x60)
    print("compasss initialized")
    compass.init_I2C()
    x=compass.bearing255()
    print("compass value with bearing255:",x)
    y=compass.bearing3599()
    print("compass value with bearing3599:",y)
    

    