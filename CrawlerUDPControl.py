# -*- coding: utf-8 -*-
"""
Created on Tue Nov 23 10:47:51 2021

@author: danny
"""

import socket

cmdFromClient       = ["MOTORS",'MOTOR:RIGHT','MOTOR:LEFT','CRAWLER:FORWARD','CRAWLER:BACKWARDS','COMPASS?']

serverAddressPort   = ("127.0.0.1", 20001)
bufferSize          = 1024

# Create a UDP socket at client side
print("Create UDP socket")
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Send to server using created UDP socket
# for cmd in cmdFromClient:
#     bytesToSend         = str.encode(cmd)
    
#     UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    
#     msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
#     msg = "Message from Server {}".format(msgFromServer[0].decode())
    
#     print(msg)

cmdCrForward = cmdFromClient[3] + " 10.4"+ " 5"
cmdMotForward = cmdFromClient[0] + " 10.1" + " 5" + " 5"

print(cmdMotForward)
bytesToSend         = str.encode(cmdMotForward)
   
UDPClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = UDPClientSocket.recvfrom(bufferSize)

msg = "Message from Server {}".format(msgFromServer[0].decode())

print(msg)