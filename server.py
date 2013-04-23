#!/usr/bin/env python
import socket
import sys
import getpass
import ipaddress


#Create a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Function that will either take the second command line argument has the server address or will ask the user to input one into the terminal
def serverAdd():
        global serverAdd
        while True:
                try:
                        serverAdd = input('Please enter server address:')
                        return ipaddress.ip_address(serverAdd)
                except ValueError:
                        print ('Invalid IP address entered')
		
# Function that will either take the third command line argument has the port number for this server to run on or will ask the user to input one into the terminal
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
                        print('Not a valid port number')
                
		
# Function that will take the fourth command line argument as the password for the server, if no password is present user will be asked to input one via the terminal		
def serverPassword():
        global password
        while True:
                try:
                        password = getpass.getpass('Please enter server password:')
                        if len(password) <=4:
                                print('Password must be longer than 4 characters, please enter password again')
                        elif password.isalnum():
                                return (password)
                        else:
                                print('Password not allowed, please try again')

                except ValueError:
                        print('Password Error!')

# Function that deals with reading and decoding password send over from user and then stores this has a global variable 
def authClient():
	global clientpass
	print ('Authenticating')
	clientpass = connection.recv(1024)
	clientpass = clientpass.decode('utf-8')
	clientpass= str(clientpass)

def getStatus():
        global alarmTriggered
        global alarmStatus
        lines = tuple(open('alarm.txt', encoding='utf-8', mode = 'r'))
        alarmTriggered = lines[1]
        alarmStatus = lines[0]
        
	
# Function that will either send detils of the alarm to the client if the password matches that of the server. If this password is incorrect a password error message will be sent to the client
def sendMessage():
        if clientpass == password:
                print('Password Accepted')
                print('Sending data to', client_address)
                alarmMessage =("Alarm Status:" + alarmStatus + "Alarm Triggered:" +alarmTriggered)
                connection.sendall(alarmMessage.encode('utf-8'))
                print('Finished sending data to', client_address)
        else:
                passerror =('Password incorrect, please try again')
                connection.sendall(passerror.encode('utf-8'))
                print('Password recieved from', client_address, 'is incorrect')
		
		
# Set up the server address, port and password		
serverAdd()
serverPort()
serverPassword()
server_address =(serverAdd, portNumber)

# Bind sever address to socket
sock.bind(server_address)

# Listen for connections, will only allow one connection to take place
sock.listen(1)


#control loop for server
while True:
	
	print ('Waiting for a connection')
	connection, client_address = sock.accept()
	try:
		print ('connection from', client_address)
		while True:
			authClient()
			getStatus()
			sendMessage()
			break
	finally:
		connection.close()




		
	
	
