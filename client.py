'''
 Filename: client.py
 Coded by: Kevin To
 Purpose - [CS372 Project 1] - File contains the client code
           written in python.
'''
#!/usr/bin/env python

import socket
import sys
import struct
import time
import clienthelper

# Check arguments
if (not clienthelper.checkArgs(sys.argv)):
	sys.exit()

# Setup socket connection
TCP_IP = sys.argv[1]
TCP_PORT = int(sys.argv[2]) 
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

handle = ""
userMessage = ""
userInput = ""
serverMessage = ""
while True:
	try:
		# Get user handle
		if not handle:
			handle = raw_input("Enter your handle: ")
			handle += "> "

		# Get user message
		userInput = raw_input(handle)
		userMessage = handle + userInput + "\n"

		# Check if user wants to close connection
		if userInput == "\quit" :
			s.send("quit\n")
			clienthelper.closeClient(s)

		s.send(userMessage)
		
		serverMessage = clienthelper.recv_timeout(s)

		# Check if server wants to close the connection
		if "\quit\n" in serverMessage:
			s.send("quit\n")
			clienthelper.closeClient(s)

		print serverMessage,

	except KeyboardInterrupt:
		clienthelper.closeClient(s)

# MESSAGE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lobortis massa et est tempor, vel finibus quam ultricies. Phasellus non neque eget purus sollicitudin dapibus. Maecenas vel enim in metus ornare bibendum. Aliquam consectetur ut ipsum et efficitur. Morbi ac convallis justo, quis convallis magna. Suspendisse sit amet gravida justo. Proin mollis, nisi et molestie sodales, elit risus vehicula erat, vitae luctus velit lorem ut nunc. Proin ac arcu hendrerit, varius dui sed orci aliquam.\n"
