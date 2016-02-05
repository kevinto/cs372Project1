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
s = clienthelper.initContact(sys.argv)

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

		clienthelper.sendUserMsgToServer(s, handle)
		
		serverMessage = clienthelper.receiveServerMsg(s)

		# Check if server wants to close the connection
		if "\quit\n" in serverMessage:
			s.send("quit\n")
			clienthelper.closeClient(s)

		print serverMessage,

	except KeyboardInterrupt:
		clienthelper.closeClient(s)

# MESSAGE = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus lobortis massa et est tempor, vel finibus quam ultricies. Phasellus non neque eget purus sollicitudin dapibus. Maecenas vel enim in metus ornare bibendum. Aliquam consectetur ut ipsum et efficitur. Morbi ac convallis justo, quis convallis magna. Suspendisse sit amet gravida justo. Proin mollis, nisi et molestie sodales, elit risus vehicula erat, vitae luctus velit lorem ut nunc. Proin ac arcu hendrerit, varius dui sed orci aliquam.\n"
