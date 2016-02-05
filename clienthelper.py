'''
 Filename: clienthelper.py
 Coded by: Kevin To
 Purpose - [CS372 Project 1] - File contains the functions
           the client code can use.
'''
'''
 Filename: client.py
 Coded by: Kevin To
 Purpose - [CS372 Project 1] - File contains helper methods for the 
                               client code. 
 '''
import socket
import sys
import struct
import time

def closeClient(s):
    s.close()
    sys.exit()

def initContact(argv):
	TCP_IP = sys.argv[1]
	TCP_PORT = int(sys.argv[2]) 
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	return s

def sendUserMsgToServer(s, handle):
	# Get user message
	userInput = raw_input(handle)
	userMessage = handle + userInput + "\n"

	# Check if user wants to close connection
	if userInput == "\quit" :
		s.send("quit\n")
		closeClient(s)

	s.send(userMessage)

def receiveServerMsg(the_socket):
    # Make socket non blocking
    the_socket.setblocking(0)
     
    # Total data partwise in an array
    total_data=[];
    data='';
    
    foundNull = False 

    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        # if total_data and time.time()-begin > timeout:
        if total_data and foundNull:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()

                # Check for null termination
                if '\n' in data:
                    foundNull = True
            else:
                #sleep for sometime to indicate a gap
                time.sleep(0.1)
        except:
            pass
     
    #join all parts to make final string
    return ''.join(total_data)

def checkArgs(argv):
	if len(argv) != 3:
		print 'Error: Server Hostname and port number required'
		return False

	port = 0
	try:
		port = int(argv[2])
	except:
		print 'Error: Port has to be a number'

	if port < 1024 or 65535 < port:
		print 'Error: Port has to be in the range 1024 to 65525'
		return False

	return True

