Prerequisites:
- This code is tested on the flip server, so make sure you run it there.
- Java and Python are required for this code to be executed.

How to compile the server code:
1. Go to the folder containing the server code.
2. Type: 
		javac server.java 

How to start the client and server executables:
1. Open two terminal windows and SSH into the same flip server. For example, flip1.engr.oregonstate.edu on port 22.
2. In both terminal windows, navigate to the folder containing the server/client code.
3. In the first terminal window, run the server code by typing (make sure you compiled the server code):
	java server <port#>
4. In the second terminal window, run the client code by typing:
	python client.py localhost <port#>
5. Enter your user handle into the client window, then enter your message. Press enter to send.
6. View the client's message on the server window.
7. Write your message in the server window to respond to the client. Press enter to send.

How to close client connection:
1. If it is the client's turn to write a message, type "\quit" (without the quotations) to terminate the client connection.
2. If it is the server's turn to write a message, type "\quit" (without the quotations) to terminate the client connection.
3. If it is the server's turn to write a message, the user can type control-c (the terminate sequence) to terminate the server and the client at the same time.
4. If it is not the server's turn to write a message and the server user types control-c, the server should terminate. When the client trys to send the server a message, the client should gracefully terminate.

Notes:
- <port#> means port number. The valid ranges are 1024 - 65535. I typically choose something like 33555.
- All references to other sources I used as information are in the source code itself. They are in the function headers
- If you are hosting the server code on another flip server, replace the "localhost" parameter in the client program argument with the server address. For example, flip2.engr.oregonstate.edu

Quick start:

Client:
	python client.py <server-hostname> <port#>

Server:
	java server <port#>
