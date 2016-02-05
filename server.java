/*****************************************************************
 * *  Filename: server.java
 * *  Coded by: Kevin To
 * *  Purpose - [CS372 Project 1] - File contains the server code
 * *            written in Java.
 * ***************************************************************/
import java.io.*;
import java.net.*;
import java.util.Scanner;

class server
{
	// This is the main entry point
	public static void main(String argv[]) throws Exception
	{
		if (!serverArgsValid(argv))
		{
			return;
		}

		startUpServer(argv);
	}

	// Purpose: To run the server
	// Params:
	//		String argv[] - command line args 
	private static void startUpServer(String argv[]) throws Exception
	{
		// Set up sockets
		ServerSocket welcomeSocket = new ServerSocket(Integer.parseInt(argv[0]));
		Socket connectionSocket = welcomeSocket.accept();
	    
	    // Set up server user input
	    Scanner reader = new Scanner(System.in);

		String clientSentence;
	    String message = "";
		while(true)
		{
	    	DataOutputStream clientSender = new DataOutputStream(connectionSocket.getOutputStream());
			
	    	clientSentence = receiveMessage(connectionSocket);

			if (clientSentence.equals("quit"))
			{
				// Need to research why we need to accept again after quit
				connectionSocket = welcomeSocket.accept();
				continue;
			}

			// Print client message
			System.out.println(clientSentence);

			// Get server message from user
		   	System.out.print("ServerUser> ");
 		   	message = "ServerUser> " + reader.nextLine();
 		   	message += '\n';

			clientSender.writeBytes(message);
		}
	}

	// Purpose: To receive the message from the socket input stream
	// Params:
	//		Socket connectionSocket - The socket to get the input stream from
	private static String receiveMessage(Socket connectionSocket) throws Exception
	{
		BufferedReader clientReader = 
			new BufferedReader(new InputStreamReader(connectionSocket.getInputStream()));

		return clientReader.readLine();
	}
	
	// Purpose: To validate server command line args
	// Params:
	//		String argv[] - command line args 
	private static boolean serverArgsValid(String argv[])
	{
		if (argv.length != 1) 
		{
			System.out.println("Error: Only one command line argument is accepted");
			return false;
		}

		int portNumber = 0;
		try
		{
			// Convert port to an int
			portNumber = Integer.parseInt(argv[0]);
		}
		catch (NumberFormatException e)
		{
			System.out.println("Error: Port needs to be a number");
			return false;
		}

		// Only valid port numbers are 1024+ because all the lower numbered
		// ports require root access
		if (1024 <= portNumber && portNumber <= 65535)
		{
			return true;
		}
		else
		{
			System.out.println("Error: Port number not within the range 1024 to 65535");
			return false;
		}
	}
}
