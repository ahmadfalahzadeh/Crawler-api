import datetime
import config #made by girls
from time import sleep
from compass import COMPASS #made by girls

CP = COMPASS(config.I2C_adresse)

while(True):
	currentPosition = CP.bearing3599()
	print("%.2f" %currentPosition)
	sleep(1)