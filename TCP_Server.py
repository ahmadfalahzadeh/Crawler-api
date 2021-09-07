import socket
import threading
import os
import json
import config
from time import sleep
from datetime import timedelta
import datetime
from crawler import CRAWLER
from compass import COMPASS
from motor import MOTOR

## Crawler type object
CR = CRAWLER()
## Compass type object
CP = COMPASS(config.I2C_adresse)
## Motor type objet (motor right)
MR = MOTOR(config.motor_right_IO2,config.motor_right_DIR,0)
## Motor type objet (motor left)
ML = MOTOR(config.motor_left_IO2,config.motor_left_DIR,1)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)        
sock.bind(('',10000))           # Client-server link
sock.listen(1)                  # Listen for incoming connections

print("[+] Listening..." )
while True:
    print('[+] Waiting for a client connection')
    connection, client_address = sock.accept()    # Connection established
    try:
            print('[+] Connection from', client_address)
            # Receive the data and retransmit it
            while True:
                 data = connection.recv(100)
                 text_file=open("trama_test.txt","a+") # Create '.txt' append type
                 text_file.write(data)                 # Write data in text_file
                 print('[+] received "%s"' % data)     # Print received data
                 data_aux=int(data)   
                 if data_aux:
                     # Evaluating received data type
                     print('[+] I have received "%s" as an int' % data_aux) 
                     if data_aux==1: #Forward movement
                        print("[+] I should be going forward")
                        CR.forward(int(100)) 
                     if data_aux==2: #Backward movement
                        CR.backward(int(100))
                        print("[+] I should be going backward")
                     if data_aux==3: #Right movement
                        CR.right(int(50))
                        print("[+] I should be going to the right")
                     if data_aux==4: #Left movement
                        CR.left(int(75))
                        print("[+] I should be going to the left")
                     if data_aux==5: #Stop movement
                        print("[+] I should be going nowhere")
                        CR.backward(int(0))
                     if data_aux==6: #Stop movement+closed conection
                        print("[+] Stop CRAWLER and closed Conection")
                        CR.backward(int(0))
                        CR.on_off(int(0))
                     connection.sendall(data)
                     print('Sending data back to the client')	
                 else:
                     print('No more data from', client_address)
                     break            
    finally:
            print('Closed conection with: ', client_address)            

