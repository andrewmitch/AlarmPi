#!/usr/bin/env python

import sys
import socket
import ipaddress
import getpass

#Create socket for client
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Requests an IP address to be entered relating to the server the client wishes to connect to, the input is checked using the ipaddress module to insure the input entered is an IP address otherwise an the ValueError caluse will be executed
def serverAdd():
    global serverAddress
    while True:
        try:
            serverAddress = input('Please enter server address:')
            return ipaddress.ip_address(serverAddress)
        except ValueError:
            print("Not a Valid IP address")
            
# Handles the port number entered by the client and checks that it is within the specified range otherwise an error statment is displayed before asking the user to input the port number again
def serverPort():
    global portNumber
    while True:
        try:
            portNumber = int(input('Please enter port number for server:'))
            if portNumber in range (0,1023):
                print('Not a suitable port number, may be taken by Operating System')
            elif portNumber in range (1024,65536):
                return int(portNumber)
            else:
                print('Not a valid port number')
        except ValueError:
            print("Not a valid port number")
        
# This Function is used to handle the password being input by the client, runs a few checks to confirm the password is acceptable
def serverPassword():
    global serverPass
    while True:
        try:
            serverPass = getpass.getpass('Please enter password for the server:')
            if len(serverPass) <=4:
                print('Password not valid, server password must be greater than 4 characters.')
            elif serverPass.isalnum():
                return(serverPass)
            else:
                print('Error, server password can only include numbers or letters, please try again')
        except ValueError:
            print("Error occurred, when entering password")
       
# Call functions that relate to server details
serverAdd()
serverPort()
serverPassword()
server_address = (serverAddress, portNumber)
print ('connecting to %s on port %s' % server_address)

# Connect this client socket to the server
sock.connect(server_address)
passwordMsg = str(serverPass)

try:
        sock.sendall(passwordMsg.encode('utf-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
finally:
        print('closing socket')
        sock.close()
