package org.usfirst.frc.team1559.robot;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class test {

	public static void main(String[] args) {
		
		try {
			  
	    	String sentence;
	        String modifiedSentence;
	        BufferedReader inFromUser = new BufferedReader(new InputStreamReader(System.in));
	
	        Socket clientSocket = new Socket("10.15.59.6", 15559);
	        DataOutputStream outToServer = new DataOutputStream(clientSocket.getOutputStream());
	        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
	
	        sentence = inFromUser.readLine();
	        outToServer.writeBytes(sentence + '\n');
	        modifiedSentence = inFromServer.readLine();
	        System.out.println(modifiedSentence);
	        clientSocket.close();
		} catch (Exception e){
			e.printStackTrace();
		}
	}

}
