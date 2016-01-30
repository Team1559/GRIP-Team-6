package org.usfirst.frc.team1559.robot;

import edu.wpi.first.wpilibj.networktables.NetworkTable;
import java.util.logging.Logger;
import java.util.logging.Level;

public class NetworkTableClient {

	public NetworkTableClient(){
		
	}
	
	public void run() {
		
		NetworkTable.setClientMode();
		NetworkTable.setIPAddress("10.15.59.23");
		NetworkTable table = NetworkTable.getTable("Contours Report");
		
		while(true){
			try{
				Thread.sleep(1000);
			}catch(Exception ex){
				Logger.getLogger(NetworkTableClient.class.getName()).log(Level.SEVERE, null, ex);
			}
			
			double cx = table.getNumber("cx");
			double cy = table.getNumber("cy");
			System.out.println(cx + cy);
		}
		
	}

}
