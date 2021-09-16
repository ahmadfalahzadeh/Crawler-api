class initial:
	def __init__(self):
		import config
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

		#initialization PWM
		CR.init_PWM()

		#enable PWM
		CR.PWM(1) 

		#put PWM at 0% (motors off)
		MR.duty_cycle(100,config.motor_right_PWM) #right motor
		ML.duty_cycle(100,config.motor_left_PWM) #left mot
