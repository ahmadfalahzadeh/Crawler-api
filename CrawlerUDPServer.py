# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 09:45:20 2021

@author: danny
"""
import socket
import time
import config #made by girls
from crawler import CRAWLER #made by girls
from compass import COMPASS #made by girls
from motor import MOTOR #made by girls
from corrector import CORRECTOR
 


#call classes
## crawler type object
CR = CRAWLER()
## corrector type object
COR = CORRECTOR()
## compass type object
CP = COMPASS(config.I2C_adresse)

## motor type objet (motor right)
MR = MOTOR(config.motor_right_IO2,config.motor_right_DIR,0)
## motor type objet (motor left)
ML =MOTOR(config.motor_left_IO2,config.motor_left_DIR,1)

# Enable use of PWM
CR.PWM(int(1))

localIP     = "192.168.1.2"
localPort   = 20001
bufferSize  = 1024

msgFromServer       = "Hello UDP Client"


# Create a datagram socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")

        
# Listen for incoming datagrams
while(True):

    message, address = UDPServerSocket.recvfrom(bufferSize)
    cmd = message.decode()
    clientMsg = "Message from Client: {}".format(message.decode())
    clientIP  = "Client IP Address:{}".format(address)

    print(clientMsg)
    print(clientIP)
    

    if cmd.startswith('MOTORS'):
        data = cmd.split(" ")
        print(data)
        if(len(data)<4):
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("COMMAND ERROR"), address) 
        else:
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("MOTORS ON"), address)
            time_on = data[1]
            speed1 = data[2]
            speed2 = data[3]
            print(float(time_on))
            print(float(speed1))
            print(float(speed2))
            
            if int(speed1)>= 0 and int(speed2)>= 0:
                MR.DIR(config.motor_right_DIR, int(1))
                ML.DIR(config.motor_left_DIR, int(0)) 
                MR.duty_cycle(int(speed1),config.motor_right_PWM)
                ML.duty_cycle(int(COR.corrector1(int(speed2))),config.motor_left_PWM)
            elif int(speed1)<= 0 and int(speed2)<= 0:
                MR.DIR(config.motor_right_DIR, int(0))
                ML.DIR(config.motor_left_DIR, int(1)) 
                MR.duty_cycle(-int(speed1),config.motor_right_PWM)
                ML.duty_cycle(int(COR.corrector2(-int(speed2))),config.motor_left_PWM)
            elif int(speed1)>= 0 and int(speed2)<= 0:
                MR.DIR(config.motor_right_DIR, int(1))
                ML.DIR(config.motor_left_DIR, int(1)) 
                MR.duty_cycle(int(speed1),config.motor_right_PWM)
                ML.duty_cycle(-int(speed2),config.motor_left_PWM)
            elif int(speed1)<= 0 and int(speed2)>= 0:
                MR.DIR(config.motor_right_DIR, int(0))
                ML.DIR(config.motor_left_DIR, int(0)) 
                MR.duty_cycle(-int(speed1),config.motor_right_PWM)
                ML.duty_cycle(int(speed2),config.motor_left_PWM)
                
            else :
                CR.forward(0)
                print("Speed 1 or 2 < 0")
                
            CR.on_off(1)
            time.sleep(float(time_on))
            CR.on_off(0)
            CR.forward(0)
    
    if cmd.startswith('MOTOR:RIGHT'):
        data = cmd.split(" ")
        print(data)
        if(len(data)<3):
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("COMMAND ERROR"), address)
        else:
            UDPServerSocket.sendto(str.encode("MOTOR:RIGHT ON"), address)
            time_on = data[1]
            speed = data[2]
            print(float(time_on))
            print(float(speed))
            time.sleep(float(time_on))
        
    if cmd.startswith('MOTOR:LEFT'):
        data = cmd.split(" ")
        print(data)
        if(len(data)<3):
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("COMMAND ERROR"), address)
        else:
            UDPServerSocket.sendto(str.encode("MOTOR:LEFT ON"), address)
            time_on = data[1]
            speed = data[2]
            print(float(time_on))
            print(float(speed))
            time.sleep(float(time))
        
    if cmd.startswith('CRAWLER:FORWARD'):
        data = cmd.split(" ")
        print(data)
        if(len(data)<3):
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("COMMAND ERROR"), address)
        else:
            UDPServerSocket.sendto(str.encode("CRAWLER:FORWARD ON"), address)
            time_on = data[1]
            speed = data[2]
            print(float(time_on))
            print(float(speed))
            time.sleep(float(time))
            
    if cmd.startswith('CRAWLER:BACKWARDS'):
        data = cmd.split(" ")
        print(data)
        if(len(data)<3):
            # Sending a reply to client
            UDPServerSocket.sendto(str.encode("COMMAND ERROR"), address)
        else:
            UDPServerSocket.sendto(str.encode("CRAWLER:BACKWARDS ON"), address)
            time_on = data[1]
            speed = data[2]
            print(float(time_on))
            print(float(speed))
            time.sleep(float(time_on))
        
    if cmd.startswith('COMPASS?'):
        msgFromServer = str(CP.bearing3599())
        print(msgFromServer)
        UDPServerSocket.sendto(str.encode(msgFromServer), address)