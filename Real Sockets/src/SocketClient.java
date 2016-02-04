

import java.io.*;
import java.net.*;

public class SocketClient {
    
	public SocketClient() {
		
	}
        
	public static void main(String[] args){
		for (int i = 0; i < 100; i++){
			String [] in = new SocketClient().read();
			System.out.println(in[0]);
			System.out.println(in[1]);
			try{
				Thread.sleep(1000);
			} catch (Exception e){
				e.printStackTrace();
			}
		}
	}
	public String[] read(){
		try {
  
	        String modifiedSentence;
	        String modifiedSentence1;
	
	        Socket clientSocket = new Socket("10.15.59.6", 15559);
	        BufferedReader inFromServer = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
	        modifiedSentence = inFromServer.readLine();
	        modifiedSentence1 = inFromServer.readLine();
	        String[] args = new String[2];
	        args[0] = modifiedSentence;
	        args[1] = modifiedSentence1;
	        clientSocket.close();
	        return args;
		} catch (Exception e){
			System.out.println("HEY MOM, I FOUND AN EXCEPTION");
			e.printStackTrace();
			return null;
		}
	}
}
