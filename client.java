/**************************************************************
 * *  Filename: smallsh.c
 * *  Coded by: Kevin To
 * *  Purpose - Implementation of a shell.
 * *
 * ***************************************************************/
import java.io.*;
import java.net.*;

class client
{
	public static void main(String argv[]) throws Exception
	{
		String sentence;
		String modifiedSentence;
		BufferedReader inFromUser = new BufferedReader( new InputStreamReader(System.in));   
		Socket clientSocket = new Socket("localhost", 33555);
		DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
		BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
		sentence = inFromUser.readLine();
		outToServer.writeBytes(sentence + '\n');
		modifiedSentence = inFromServer.readLine();
		System.out.println("FROM SERVER: " + modifiedSentence);
		clientSocket.close();	
	}
}