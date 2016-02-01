'''
 Filename: clienthelper.py
 Coded by: Kevin To
 Purpose - [CS372 Project 1] - File contains the functions
           the client code can use.
'''
import socket
import sys
import struct
import time

def recv_timeout(the_socket,timeout=2):
    # Make socket non blocking
    the_socket.setblocking(0)
     
    # Total data partwise in an array
    total_data=[];
    data='';
     
    #beginning time
    begin=time.time()
    while 1:
        #if you got some data, then break after timeout
        if total_data and time.time()-begin > timeout:
            break
         
        #if you got no data at all, wait a little longer, twice the timeout
        elif time.time()-begin > timeout*2:
            break
         
        #recv something
        try:
            data = the_socket.recv(8192)
            if data:
                total_data.append(data)
                #change the beginning time for measurement
                begin=time.time()
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
